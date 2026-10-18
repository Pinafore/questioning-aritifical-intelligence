# Chapters 7–9: deduplication and citation review

2026-10-18. New citation proposals below are pending author review, not inserted into LaTeX. The existing HotpotQA citation was relocated from Chapter 9 to its introduction in Chapter 7; the existing Dan Russell blog URL was converted into a footnote. No bibliography entries were added in this pass.

## Changes made

- Removed Chapter 8's second introductory dataset survey, preserving its unique NarrativeQA and HotpotQA summaries before Conversational Datasets.
- Kept Chapter 7's QBLink/Bitcoin example and fuller discussion of conversational evaluation. Consolidated QuAC, CANARD, and CoQA collection descriptions in Chapter 8, with cross-references.
- Kept Chapter 9's more developed Lotto and Egypt/Israel evidence walkthroughs; Chapter 7 retains the Dario Fo example and points forward. Planning now revisits the Egypt/Israel evidence without restating the question.
- Moved Chapter 7's multihop algorithm survey to Chapter 9 after the evidence walkthrough. Replaced the repeated answer-string-versus-evidence explanation with a reference to Windsor.
- Kept the Apu dialogue and scoring discussion in Chapter 9. Removed the duplicate conversation/Georgia motivation from Chapter 9 in favor of a reference to Chapter 7.
- This is a deduplication pass, not the planned comprehensive factual, citation, or style update. Historical capability claims and unfinished examples still need review.

## Proposed citations at the retained passages

Locations use section names and distinctive paragraph text so they remain findable as line numbers change. Paper identities are checked against the linked primary sources; the specific numerical and example claims still need checking when citations are inserted.

| Location | Proposed paper and authors | Review note |
|---|---|---|
| Ch. 7, Conversational QA: introducing QBLink before Bitcoin | [A dataset and baselines for sequential open-domain question answering](https://aclanthology.org/D18-1134/) (2018). Ahmed Elgohary, Chen Zhao, Jordan Boyd-Graber. | Cite at the dataset introduction. |
| Ch. 8, Conversational Datasets: QuAC paragraph | [QuAC: Question Answering in Context](https://aclanthology.org/D18-1241/) (2018). Eunsol Choi, He He, Mohit Iyyer, Mark Yatskar, Wen-tau Yih, Yejin Choi, Percy Liang, Luke Zettlemoyer. | Existing bibliography key `choi-18`. |
| Ch. 8, Conversational Datasets: question rewriting/CANARD | [Can You Unpack That? Learning to Rewrite Questions-in-Context](https://aclanthology.org/D19-1605/) (2019). Ahmed Elgohary, Denis Peskov, Jordan Boyd-Graber. | Existing key `elgohary-19`. |
| Ch. 8, Conversational Datasets: CoQA paragraph | [CoQA: A Conversational Question Answering Challenge](https://aclanthology.org/Q19-1016/) (2019). Siva Reddy, Danqi Chen, Christopher D. Manning. | Existing `reddy-18` record says 2018, but TACL publication is 2019. Review the claim that it appeared a year after QuAC: both preprints appeared in 2018. |
| Ch. 8, Other Reading Datasets: NarrativeQA | [The NarrativeQA Reading Comprehension Challenge](https://aclanthology.org/Q18-1023/) (2018). Tomáš Kočiský, Jonathan Schwarz, Phil Blunsom, Chris Dyer, Karl Moritz Hermann, Gábor Melis, Edward Grefenstette. | Preserved from the deleted survey's unique tail. |
| Ch. 9, Learning to Find the Next Hop: DELFT | [Complex Factoid Question Answering with a Free-Text Knowledge Graph](https://www.cs.umd.edu/~jbg/docs/2020_www_delft.pdf). Chen Zhao, Chenyan Xiong, Xin Qian, Jordan Boyd-Graber. | Confirm whether the adjacent “this paper from Chen et al.” means this same paper or a separate work. |
| Same subsection: Transformer-XH | [Transformer-XH: Multi-Evidence Reasoning with eXtra Hop Attention](https://www.microsoft.com/en-us/research/wp-content/uploads/2020/01/transformer_xh_multi_evidence_reasoning_with_extra_hop_attention.pdf) (2020). Chen Zhao, Chenyan Xiong, Corby Rosset, Xia Song, Paul Bennett, Saurabh Tiwary. | Check the later top-10/90% claim separately; identifying the paper does not verify that number. |
| Same subsection: Golden Retriever / explicit queries | [Answering Complex Open-domain Questions Through Iterative Query Generation](https://aclanthology.org/D19-1261/) (2019). Peng Qi, Xiaowen Lin, Leo Mehr, Zijian Wang, Christopher D. Manning. | Check the Armada worked example against the paper. |
| Same subsection: Inoue / concise explanations | [Summarize-then-Answer: Generating Concise Explanations for Multi-hop Reading Comprehension](https://aclanthology.org/2021.emnlp-main.490/) (2021). Naoya Inoue, Harsh Trivedi, Steven Sinha, Niranjan Balasubramanian, Kentaro Inui. | Proposed source for the Northern Lights example. |
| Same subsection: Xiong / vector queries | [Answering Complex Open-Domain Questions with Multi-Hop Dense Retrieval](https://arxiv.org/abs/2009.12756) (ICLR 2021). Wenhan Xiong, Xiang Lorraine Li, Srini Iyer, Jingfei Du, Patrick Lewis, William Yang Wang, Yashar Mehdad, Wen-tau Yih, Sebastian Riedel, Douwe Kiela, Barlas Oğuz. | Distinguish Wenhan Xiong from Chenyan Xiong. |
| Same subsection: Chen Zhao / training without evidence annotations | [Distantly-Supervised Dense Retrieval Enables Open-Domain Question Answering without Evidence Annotation](https://aclanthology.org/2021.emnlp-main.756/) (2021). Chen Zhao, Chenyan Xiong, Jordan Boyd-Graber, Hal Daumé III. | Anthology title differs from the PDF/preprint's “Distantly-Supervised Evidence Retrieval Enables Question Answering without Evidence Annotation”; confirm preferred title. Check the quantitative comparison separately. |
| Same subsection: Jiang and Bansal / reasoning shortcuts | [Avoiding Reasoning Shortcuts: Adversarial Evaluation, Training, and Model Development for Multi-Hop QA](https://arxiv.org/abs/1906.07132) (2019). Yichen Jiang, Mohit Bansal. | Proposed source for adversarial supporting documents. |
| Same subsection: DiRe | [Is Multihop QA in DiRe Condition? Measuring and Reducing Disconnected Reasoning](https://aclanthology.org/2020.emnlp-main.712/) (2020). Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, Ashish Sabharwal. | Review the manuscript's description of what the probe measures before inserting. |

## Existing citation relocated

Chapter 7, Multihop QA: *HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering* (2018), Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov, Christopher D. Manning. Existing key `Yang2018HotpotQAAD` retained with the introduction rather than the removed duplicate in Chapter 9.

## Still needs author identification

- The potentially separate “Chen et al.” link-following paper beside DELFT.
- The “Guha et al. 2015” annotation paper in the retained Chapter 8 HotpotQA summary. No guessed citation inserted.
- Earlier unresolved methods citations (Dagan/Socher, Hinton, process rewards/verifiers) remain tracked in `methods-review.md`; no new proposals for those in this batch.
