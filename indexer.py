import json
import math
from preprocessor import preprocess

class Indexer:
    def __init__(self):
        self.index = {}       # word -> {doc_id: term_frequency}
        self.docs = {}        # doc_id -> original text
        self.doc_count = 0

    def add_document(self, text):
        doc_id = self.doc_count
        self.docs[doc_id] = text
        self.doc_count += 1

        tokens = preprocess(text)
        token_count = len(tokens)

        for token in tokens:
            tf = tokens.count(token) / token_count
            if token not in self.index:
                self.index[token] = {}
            self.index[token][doc_id] = tf

    def save(self, path='index.json'):
        with open(path, 'w') as f:
            json.dump({'index': self.index, 'docs': self.docs}, f)

    def load(self, path='index.json'):
        with open(path, 'r') as f:
            data = json.load(f)
        self.index = data['index']
        self.docs = {int(k): v for k, v in data['docs'].items()}
        self.doc_count = len(self.docs)