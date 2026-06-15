import json
from indexer import Indexer
from searcher import Searcher

def load_arxiv_papers(filepath, category_filter='cs.LG', max_papers=5000):
    papers = []
    with open(filepath, 'r') as f:
        for line in f:
            if len(papers) >= max_papers:
                break
            try:
                paper = json.loads(line)
                if category_filter in paper.get('categories', ''):
                    text = f"{paper['title']}. {paper['abstract']}"
                    papers.append(text.replace('\n', ' '))
            except:
                continue
    return papers

print("Loading ArXiv ML papers...")
filepath = 'C:\\Users\\senga\\Downloads\\arxiv-metadata-oai-snapshot.json'
documents = load_arxiv_papers(filepath, category_filter='cs.LG', max_papers=5000)
print(f"Loaded {len(documents)} papers")

indexer = Indexer()
for i, doc in enumerate(documents):
    indexer.add_document(doc)
    if i % 500 == 0:
        print(f"Indexed {i}/{len(documents)}")
indexer.save()

searcher = Searcher(indexer)

print("\nMini Search Engine — ArXiv ML Papers")
print("=" * 40)

while True:
    query = input("\nEnter search query (or 'quit' to exit): ")
    if query.lower() == 'quit':
        break
    
    results = searcher.search(query)
    
    if not results:
        print("No results found.")
    else:
        print(f"\nTop {len(results)} results:")
        for i, r in enumerate(results):
            print(f"\n{i+1}. Score: {r['score']}")
            print(f"   {r['text']}...")