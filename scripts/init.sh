python3 -m venv venv
pip install -U pip
pip install -r requirements.txt
python3 -c "import nltk; nltk.download('wordnet')"