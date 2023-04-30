import json
from argparse import ArgumentParser
from pathlib import Path
from typing import Dict, Union

from bs4 import BeautifulSoup

from wnsub.wordnet import get_wn_substitutes


def read_raganato_labels(path: Union[str, Path]) -> Dict[str, str]:
    labels = {}
    with open(path, "r") as f:
        for line in f:
            instance_id, wn_key, *other = line.strip().split(" ")
            labels[instance_id] = wn_key

    return labels


def build_lexsub_dataset(
    xml_path: str,
    labels_path: str,
    output_path: str,
):
    labels = read_raganato_labels(labels_path)

    with open(xml_path, "r") as f, open(output_path, "w") as o:
        soup = BeautifulSoup(f, "xml")

        for s in soup.find_all("sentence"):
            items = [item for item in s if item.name is not None]
            tokens = [item.text for item in items]

            for idx, item in enumerate(items):
                if item.name == "instance":
                    gold_sense_key = labels[item["id"]]
                    substitutes = get_wn_substitutes(gold_sense_key)

                    if len(substitutes) == 0:
                        continue

                    output = {
                        "id": item["id"],
                        "context": tokens,
                        "target_idx": idx,
                        "lemma": item["lemma"],
                        "pos": item["pos"],
                        "substitutes": substitutes,
                    }

                    o.write(json.dumps(output) + "\n")


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--xml_path", type=str, required=True)
    parser.add_argument("--labels_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)

    args = parser.parse_args()

    build_lexsub_dataset(
        xml_path=args.xml_path,
        labels_path=args.labels_path,
        output_path=args.output_path,
    )


if __name__ == "__main__":
    main()
