#!/bin/bash
XLM_PATH=$(realpath data/SemCor/semcor.data.xml)
LABELS_PATH=$(realpath data/SemCor/semcor.gold.key.txt)

mkdir -p data/wnsub
OUTPUT_PATH=$(realpath data/wnsub/wnsub.jsonl)

# Prepare virtual environment
source venv/bin/activate

# Run the script
python3 -m wnsub.build_wnsub  \
    --xml_path $XLM_PATH \
    --labels_path $LABELS_PATH \
    --output_path $OUTPUT_PATH