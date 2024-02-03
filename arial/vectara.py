import arxiv
import shutil
from llama_index import Document
from llama_index.indices import VectaraIndex
import os 

client = arxiv.Client()
search = arxiv.Search(
  query = "(ti:embedding model) OR (ti:sentence embedding)",
  max_results = 100,
  sort_by = arxiv.SortCriterion.Relevance
)
papers = list(client.results(search))

data_folder = 'temp'
os.makedirs(data_folder, exist_ok=True)

# Create Vectara Index
index = VectaraIndex()

# Upload content ofr all papers
for paper in papers:
    try:
        paper_fname = paper.download_pdf(data_folder)
    except Exception as e:
        print(f"File {paper_fname} failed to load with error {e}")
        continue
    metadata = {
        'url': paper.entry_id,
        'title': paper.title,
        'author': str(paper.authors[0]),
        'published': str(paper.published.date())
    }        
    index.insert_file(file_path=paper_fname, metadata=metadata)

shutil.rmtree(data_folder)