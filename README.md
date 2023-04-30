# WNSub
This repository contains code for the WNSub lexical substitution dataset. The dataset was generated automatically from SemCor 3.0 and WordNet by retrieving synonyms corresponding to the gold senses of the target words.

## Data
The dataset is available at `data/wnsub/wnsub.jsonl`. Each line in the file contains a JSON object with the following fields:
- **id**: a unique identifier for the instance
- **context**: the context sentence containing the target word
- **target_idx**: the index of the word to be substituted
- **lemma**: lemma of the target word
- **pos**: PoS tag of the target words
- **substitutes**: a list of substitutes retrieved from WordNet

## Building
To build the dataset from scratch, follow these steps:

1. Install the necessary dependencies in a virtual environment by running the following command:
```bash
bash scripts/init.sh
```

2. Build the dataset by running the following command:
```bash
bash scripts/build_wnsub.sh
```

## Acknowledgement
SemCor 3.0 dataset accessed through WSD evaluation frameword (Raganato et al., 2017)

```
Alessandro Raganato, José Camacho-Collados and Roberto Navigli. Word Sense Disambiguation: A Unified Evaluation Framework and Empirical Comparison In Proceedings of European Chapter of the Association for Computational Linguistics (EACL), Valencia, Spain, April 3-7, 2017. 
```