# Methods script: author follow-up

The 2026-09-21 pass rewrites existing script material, removes its repeated
dense-retrieval block, adds real section labels and cross-references, and
consolidates ROUGE here from formats. It does not supply missing lecture examples,
figures, equations, or a Transformer tutorial.

## Citations needing identification or confirmation

- Dagan and Glickman (2004) is now confirmed and cited for the common entailment framework; see the 2026-10-18 follow-up in chapters-7-9-citation-review.md. McCann et al. (2018), supplied for Socher, is now cited for casting ten NLP tasks as QA; the unsupported AI-completeness attribution was removed.
- The paper intended for training mathematical reasoning with intermediate
  rewards/verifiers. Wei et al. (2022) supports chain-of-thought prompting;
  it does not establish the subsequent training claim.
- The exact source for Hinton's preference for “confabulation”, if retaining
  this attributed aside.
- The 2015 presidential-embedding projection: Iyyer et al. is the obvious
  citation for deep averaging networks, but confirm the slide/example provenance.

## Material for the author to supply or decide

- Start/end probabilities for the now-supplied Windsor example, if retaining
  the proposed scored-span illustration. Do not invent model probabilities.
- The presidential-embedding figure and additional Cairo/Mossad evidence passages.
- The preference-ranking figure and alignment-dataset examples, if desired. Encoder and decoder explanations are now adapted from the shared lecture scripts; the schematic reward/KL objective is in Chapter 10.
- The Egypt/Israel scratchpad now uses the existing Cairo/Mossad evidence;
  the unsupported border assumption and unnecessary identity placeholder are gone.
- Identify the science-fiction scene in the commented YouTube link.
- There is also repeated multihop material (Lotto and Egypt/Israel) and the Apu
  dialogue across formats and methods. Decide which chapter should own each;
  this pass only consolidates the specifically requested ROUGE material.

## Technical corrections to review

- Exact high-dimensional search is expensive, not impossible.
- Min-wise hashing estimates set similarity; the script had conflated it with
  arbitrary cosine-based vector compression.
- The in-batch-negative discussion is attributed to DPR, not REALM.
- BERT is an encoder option, rather than a claim about what everyone uses today.
- BLEU uses modified n-gram precision and a brevity penalty; it is not a
  precision/recall combination.
- Preference training now distinguishes reward scores from policy probabilities
  and a reward model from a value function. Confirm this is the intended RLHF
  account rather than an intended explanation of direct preference optimization.
- The T5 example illustrates its objective; it no longer claims the model saw
  that exact Allen Iverson sentence during training.

## Citation provenance

Reused existing records for BERT, deep averaging networks, ORQA, Natural
Questions, EfficientQA, BLEU, and ROUGE. Added 11 records:

- DPR (`karpukhin-20`), recovered from the supplied jbg.bib and checked against
  https://aclanthology.org/2020.emnlp-main.550/
- HotpotQA (`Yang2018HotpotQAAD`), recovered from the supplied qanta.bib.
- REALM (`guu-20`): https://proceedings.mlr.press/v119/guu20a.html
- ROUGE critique (`krishna-21`): https://aclanthology.org/2021.naacl-main.393/
- PEDANTS (`li-etal-2024-pedants`): https://aclanthology.org/2024.findings-emnlp.548/
- T5 (`raffel-20`): https://www.jmlr.org/papers/v21/20-074.html
- RLHF (`ouyang-22`): https://arxiv.org/abs/2203.02155
- Chain of thought (`wei-22`): https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html
- Bradley--Terry overview (`hunter-bradley-terry-04`): David Hunter's publication
  list, https://sites.psu.edu/drh20/david-hunters-home-page/publications/
- Approximate nearest-neighbor search (`arya-98`): author's paper at
  https://www.cse.ust.hk/faculty/arya/pub/JACM.pdf
- Min-wise permutations (`broder-98`): original STOC paper identified in the
  authors' extended paper at https://www.cs.princeton.edu/courses/archive/spring05/cos598E/bib/broder98minwise.pdf

## Validation

The source audit finds no missing citation keys or reference targets in methods
and no duplicate labels in the book. ROUGE counts were checked computationally.
A compiled PDF still needs checking; no local LaTeX compiler was available.

## Follow-up: supplied references and remaining placeholders

Added `cho-20-spolin` and `srikanth-26-discotrace` after the author identified
these papers. The supplied DiscoTrace PDF URL was inaccessible; the accessible
preprint at https://arxiv.org/html/2604.15140v1/ supports the answering-strategy
claim. The EMNLP 2026 venue and full author name follow the author's metadata.

All five literal manuscript placeholders are now resolved:

| Location | Status |
|---|---|
| Machine-reading answer year | The author supplied three Windsor questions with answer 1917 and a misleading Wikipedia passage; all are incorporated. |
| Iverson cloze | Changed XXX to an explicit underlined answer slot; the following sentence already supplies Allen Iverson. |
| Breastfeeding example attribution | Cited Pregnant Questions (Srikanth et al., 2024), Figure 1; matched the question wording and narrowed the explanation to what the source supports. |
| Communities' discourse moves | Replaced YYY with the DiscoTrace citation and wording supported by its findings. |
| Egypt/Israel scratchpad | Rewritten from existing evidence; no identity placeholder remains. |

Other unfinished material is listed above: the figures, scored spans, reward/KL
objective, optional Transformer explanation, science-fiction scene, and uncertain
Dagan/Socher, Hinton, and process-reward references remain open.


The Windsor passage is quoted from the text supplied by the author, with a
Wikipedia source link and the answer-year highlighted. The explanation now
separates a matching string from evidence for the name change; the supplied
passage contains only one occurrence of 1917, so the old repeated-year claim
was removed. No model scores have been invented.

Maternal-health source: https://aclanthology.org/2024.naacl-long.403/, Figure 1.
The script's “only way” antibody claim was removed; the revised passage describes
the paper's response and preserves the separate SPOLIN citation for the analogy.


## Encoder/decoder/RLHF reorganization (2026-10-18)

- Chapter 7 now owns retrieval and the Transformer encoder. Adapted queries/keys/values, softmax, heads, layers, position information, and CLS from the author's “Lecture Scripts” Google Doc (BERT discussion around “What are keys, values, and queries?”). Retained `sec:methods:deep-retrieval` as a compatibility alias beside `sec:formats:deep-retrieval`.
- Chapter 9 now owns the decoder. Adapted “What BERT Can’t Do: The Decoder” from the same document: causal masking, cross-attention, vocabulary prediction, teacher forcing, and exposure bias. Omitted slide-dependent diagrams and the script's incorrect implication that grammatical gender follows natural sex. Added brief connections to QA and supervised instruction tuning.
- Chapter 10 now owns Bradley–Terry preference modeling and RLHF, after Ranking and Comparing Subjects and before the empirical IRT study. Retained `sec:methods:preferences` as a compatibility alias. The RLHF coefficient is eta to avoid confusion with the IRT feasibility parameter lambda. The equation is explicitly a schematic reward-minus-KL objective, not a transcription of the full InstructGPT objective.
- Source: https://docs.google.com/document/d/1QayGOfemBnVmTgzcdOtYrdXWcenO58n5QB5bFFlYOA0/edit . Read via a browser export; the shared document itself was not edited.
- Existing citations reused: Vaswani et al. (2017), Devlin et al. (2019), Karpukhin et al. (2020), Hunter (2004), and Ouyang et al. (2022). No new bibliography entries in this reorganization.
- The earlier duplicate Lotto/Egypt/Apu issue is resolved by the preceding deduplication pass. Remaining missing figures, scored spans, scene identification, and process-reward attribution remain author follow-ups.
