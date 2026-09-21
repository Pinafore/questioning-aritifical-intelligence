# Methods script: author follow-up

The 2026-09-21 pass rewrites existing script material, removes its repeated
dense-retrieval block, adds real section labels and cross-references, and
consolidates ROUGE here from formats. It does not supply missing lecture examples,
figures, equations, or a Transformer tutorial.

## Citations needing identification or confirmation

- “Jon's paper” on accepting false premises, the source of the breastfeeding
  example, and “YYY” on communities' preferred discourse moves. The quoted
  medical explanation also needs verification against its source.
- The specific Dagan and Socher sources for the AI-completeness attributions.
- The paper intended for training mathematical reasoning with intermediate
  rewards/verifiers. Wei et al. (2022) supports chain-of-thought prompting;
  it does not establish the subsequent training claim.
- The exact source for Hinton's preference for “confabulation”, if retaining
  this attributed aside.
- The 2015 presidential-embedding projection: Iyyer et al. is the obvious
  citation for deep averaging networks, but confirm the slide/example provenance.

## Material for the author to supply or decide

- The Natural Questions running example, its passage, and start/end probabilities
  (the answer still appears as XXX in the script).
- The presidential-embedding figure and additional Cairo/Mossad evidence passages.
- The preference-ranking figure if desired, reward/KL objective, and any
  Transformer overview or alignment-dataset examples.
- Revise the Egypt/Israel scratchpad: a shared border does not follow from the
  question, and its remaining XXX needs an identity. It is retained as a draft,
  not presented as verified reasoning.
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
