from typing import List

from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import Synset


def preprocess_lemma(lemma: str) -> str:
    # lemma = wn_lemmatizer.lemmatize(lemma)
    lemma = lemma.lower().replace("_", " ")

    return lemma


def get_lemma_from_wn_key(wn_key: str) -> str:
    lemma_obj = wn.lemma_from_key(wn_key)
    lemma: str = lemma_obj.name()

    return lemma


def get_synset_from_wn_key(wn_key: str) -> Synset:
    synset: Synset = wn.lemma_from_key(wn_key).synset()
    return synset


def get_wn_substitutes(wn_key: str) -> List[str]:
    target_lemma = get_lemma_from_wn_key(wn_key)
    synset = get_synset_from_wn_key(wn_key)

    target_lemma = preprocess_lemma(target_lemma)

    substitutes = []
    unique_substitutes = set()

    for synonym in synset.lemma_names():
        processed_synonym = preprocess_lemma(synonym)
        if processed_synonym not in unique_substitutes:
            substitutes.append(processed_synonym)
            unique_substitutes.add(processed_synonym)

    if target_lemma in substitutes:
        substitutes.remove(target_lemma)

    return substitutes
