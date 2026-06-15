# Mini Search Engine

A TF-IDF based search engine built from scratch in Python, indexed on 5,000 machine learning research paper abstracts from ArXiv.

## How It Works

**TF-IDF (Term Frequency-Inverse Document Frequency):**
- TF — how often a word appears in a document
- IDF — how rare a word is across all documents
- Words that appear often in one document but rarely elsewhere get high scores
- Results ranked by TF-IDF score

**Inverted Index:**
- Maps each word → list of documents containing it
- Enables O(1) lookup instead of scanning every document

## Stack
Python · NLTK · JSON

## Dataset
5,000 ML paper abstracts from ArXiv (cs.LG category)

## Run
pip install nltk
python main.py

## Sample Queries
- "neural network optimization"
- "transformer attention mechanism"  
- "reinforcement learning reward"
- "computer vision object detection"

## Architecture
- `preprocessor.py` — tokenization, stopword removal, stemming
- `indexer.py` — builds inverted index, calculates TF scores
- `searcher.py` — calculates IDF, ranks results by TF-IDF
- `main.py` — loads dataset, runs search loop
