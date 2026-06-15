import math
from preprocessor import preprocess

class Searcher:
    def __init__(self, indexer):
        self.indexer = indexer

    def idf(self, token):
        docs_with_token = len(self.indexer.index.get(token, {}))
        if docs_with_token == 0:
            return 0
        return math.log(self.indexer.doc_count / docs_with_token)

    def search(self, query, top_k=5):
        tokens = preprocess(query)
        scores = {}

        for token in tokens:
            if token not in self.indexer.index:
                continue
            idf = self.idf(token)
            for doc_id, tf in self.indexer.index[token].items():
                tfidf = tf * idf
                scores[doc_id] = scores.get(doc_id, 0) + tfidf

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        results = []
        for doc_id, score in ranked[:top_k]:
            results.append({
                'doc_id': doc_id,
                'score': round(score, 4),
                'text': self.indexer.docs[doc_id][:200]
            })
        return results