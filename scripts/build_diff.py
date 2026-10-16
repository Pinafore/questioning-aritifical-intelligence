"""Prepare review LaTeX sources; the Makefile compiles the review PDF."""

import argparse
import io
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]


class DiffPreparationError(RuntimeError):
    pass


def run(args, cwd, *, step=None, **kwargs):
    step = step or f"Run {args[0]}"
    try:
        return subprocess.run(args, cwd=cwd, check=True, **kwargs)
    except (subprocess.CalledProcessError, OSError) as error:
        raise DiffPreparationError(
            f"{step} failed.\n"
            f"  Working directory: {cwd}\n"
            f"  Command: {subprocess.list2cmdline([str(a) for a in args])}\n"
            f"  Cause: {error}\n"
            "  See the command's output above for details."
        ) from error


def snapshot(base, old, new):
    """Read the committed tree and copy current source/assets, including new files."""
    revision = run(["git", "rev-parse", "--verify", base + "^{commit}"], ROOT,
                   step=f"Resolve baseline {base!r} (check DIFF_BASE names an existing commit)",
                   stdout=subprocess.PIPE).stdout.decode().strip()
    archive = run(["git", "archive", "--format=zip", revision], ROOT,
                  stdout=subprocess.PIPE).stdout
    with zipfile.ZipFile(io.BytesIO(archive)) as files:
        for member in files.infolist():
            target = (old / member.filename).resolve()
            if not target.is_relative_to(old.resolve()):
                raise ValueError("Git archive contains an unsafe path")
        files.extractall(old)
    names = run(["git", "ls-files", "-z", "--cached", "--others",
                 "--exclude-standard"], ROOT, stdout=subprocess.PIPE).stdout
    # Include ignored local figure/font assets, but never local_data or build output.
    paths = {Path(name.decode("utf-8")) for name in names.split(b"\0") if name}
    for directory in ("figures", "style", "bib"):
        paths.update(path.relative_to(ROOT) for path in (ROOT / directory).rglob("*")
                     if path.is_file())
    for relative in paths:
        if relative.parts[0] in {"build", "local_data", ".git"}:
            continue
        source = ROOT / relative
        if source.is_file():  # A tracked file can have been deleted locally.
            target = new / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    return revision


def generate_blurbs(tree, description="snapshot", fallback=None):
    generator = tree / "scripts" / "split_blurbs.py"
    data = tree / "chapter_blurbs.json"
    if not data.exists():
        if any((tree / "chapters" / "blurbs").glob("*.tex")):
            print(f"{description}: no chapter_blurbs.json; keeping saved blurbs.", flush=True)
            return
        raise DiffPreparationError(
            f"Cannot generate chapter blurbs for {description}:\n"
            "  Missing chapter_blurbs.json and no saved chapters/blurbs/*.tex.\n"
            "  Choose a DIFF_BASE containing the book's blurb data, or restore\n"
            "  the missing data in the working tree if this is the current snapshot."
        )
    if not generator.exists():
        if fallback is None or not fallback.is_file():
            raise DiffPreparationError(
                f"Cannot generate chapter blurbs for {description}:\n"
                f"  Missing {generator}.\n"
                "  Restore scripts/split_blurbs.py in the working tree and retry."
            )
        generator = fallback
        print(f"{description}: scripts/split_blurbs.py is absent; using the current "
              "generator with this snapshot's chapter_blurbs.json.", flush=True)
    (tree / "chapters" / "blurbs").mkdir(parents=True, exist_ok=True)
    run([sys.executable, str(generator), "--draft_sections",
         "--proposal_sections"], tree, step=f"Generate chapter blurbs for {description}")


def exclude_index_table(old, new):
    """Keep the current sample index verbatim, outside latexdiff's markup."""
    relative = Path("chapters/130-ir.tex")
    pattern = re.compile(
        r"\\begin\{(quote|center)\}\s*\\begin\{tabular\*?\}.*?"
        r"\\end\{tabular\*?\}\s*\\end\{\1\}", re.DOTALL)
    current = new / relative
    if not current.exists():
        return
    text = current.read_text(encoding="utf-8")
    table = next((m.group() for m in pattern.finditer(text)
                  if "INDEX 269" in m.group()), None)
    if table is None:
        return
    (new / "diff-index-table.tex").write_text(table + "\n", encoding="utf-8")
    for tree in (old, new):
        path = tree / relative
        if path.exists():
            text = path.read_text(encoding="utf-8")
            text = pattern.sub(lambda m: r"\input{diff-index-table.tex}"
                               if "INDEX 269" in m.group() else m.group(), text)
            path.write_text(text, encoding="utf-8")


def make_diff(old, new, destination):
    """Diff chapter bodies separately: chapterfile's dynamic inputs stay intact."""
    # Deleted text and generated blurbs can retain old capitalization. BibTeX
    # rejects two spellings of the same key, even when one is in deleted text.
    spellings = {}
    for bib in (new / "bib").glob("*.bib"):
        for key in re.findall(r"@\w+\s*\{\s*([^\s,]+)\s*,",
                              bib.read_text(encoding="utf-8")):
            spellings.setdefault(key.casefold(), set()).add(key)
    canonical = {folded: next(iter(keys)) for folded, keys in spellings.items()
                 if len(keys) == 1}
    citation = re.compile(r"(\\(?:cite\w*|nocite)\*?(?:\s*\[[^\]]*\])*\s*\{)([^{}]*)(\})")
    def normalize(match):
        keys = re.sub(r"[^,\s]+", lambda key: canonical.get(
            key.group().casefold(), key.group()), match[2])
        return match[1] + keys + match[3]
    for tree in (old, new):
        for path in [tree / "main.tex", *(tree / "chapters").rglob("*.tex")]:
            if path.exists():
                text = path.read_text(encoding="utf-8")
                updated = citation.sub(normalize, text)
                if updated != text:
                    path.write_text(updated, encoding="utf-8")
    exclude_index_table(old, new)
    shutil.copytree(new, destination, dirs_exist_ok=True)
    empty = old / "empty-for-latexdiff.tex"
    empty.write_text("", encoding="utf-8")
    sources = {Path("main.tex")}
    for tree in (old, new):
        sources.update(p.relative_to(tree) for p in (tree / "chapters").rglob("*.tex"))
    for relative in sorted(sources):
        before, after = old / relative, new / relative
        if not after.exists():
            continue  # Removed chapters are no longer included by current main.tex.
        output = destination / relative
        if relative != Path("main.tex") and before.exists() and before.read_bytes() == after.read_bytes():
            continue
        if relative == Path("main.tex"):
            output = destination / "main-diff.tex"
        output.parent.mkdir(parents=True, exist_ok=True)
        # Always process main.tex so it supplies the DIF macro definitions, even
        # when all edits are in chapters. Treat book macros' arguments as prose.
        with output.open("wb") as handle:
            # Graphics markup makes DIF boundary commands perform assignments,
            # which are illegal before a multicolumn at the start of a table cell.
            run(["latexdiff", "--encoding=utf8", "--graphics-markup=none",
                 "--append-textcmd=question,evidence,answer",
                 str(before if before.exists() else empty), str(after)],
                new, stdout=handle, step=f"Generate latexdiff markup for {relative}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="HEAD", help="baseline Git revision (default: HEAD)")
    args = parser.parse_args()
    needed = ("git", "latexdiff")
    missing = [name for name in needed if shutil.which(name) is None]
    if missing:
        parser.exit(2, "Missing build tools: " + ", ".join(missing)
                    + ". Install a TeX distribution with latexdiff and put its tools on PATH.\n")

    output = ROOT / "build" / "latexdiff"
    output.parent.mkdir(parents=True, exist_ok=True)
    # Every invocation starts clean: no stale chapters, auxiliary files, or PDFs.
    # Only delete this fixed, generated directory after checking its resolved path.
    if output.exists():
        if output.is_symlink() or output.resolve() != ROOT.resolve() / "build" / "latexdiff":
            raise ValueError("Refusing to clear a redirected output directory")
        shutil.rmtree(output)
    with tempfile.TemporaryDirectory(prefix="book-diff-") as temporary:
        old, new = Path(temporary) / "old", Path(temporary) / "new"
        old.mkdir()
        new.mkdir()
        revision = snapshot(args.base, old, new)
        print(f"Comparing baseline {args.base} ({revision[:12]}) with the working tree.", flush=True)
        generate_blurbs(old, f"baseline {args.base} ({revision[:12]})",
                        fallback=new / "scripts" / "split_blurbs.py")
        generate_blurbs(new, "current working tree")
        make_diff(old, new, output)
    (output / "baseline.txt").write_text(revision + "\n", encoding="utf-8")
    print("Review sources:", output / "main-diff.tex")


if __name__ == "__main__":
    try:
        main()
    except (DiffPreparationError, OSError, ValueError) as error:
        print("Diff source preparation failed:", error, file=sys.stderr)
        sys.exit(1)
