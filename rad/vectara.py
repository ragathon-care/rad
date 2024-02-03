import arxiv
import shutil
from llama_index.indices import VectaraIndex, VectorStoreIndex
from llama_index.service_context import ServiceContext
import os 
from llama_index.embeddings import HuggingFaceEmbedding

from dotenv import load_dotenv
import pathlib
print('loading .env')
load_dotenv(dotenv_path=pathlib.Path(__file__, '../.env'))

client = arxiv.Client()
search = arxiv.Search(
  query = "(ti:embedding model) OR (ti:sentence embedding)",
  max_results = 5,
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

query = "What is sentence embedding?"
query_engine = index.as_query_engine(similarity_top_k=5)
response = query_engine.query(query)
print(response)

query_engine = index.as_query_engine(
    similarity_top_k=5,
    vectara_query_mode="mmr",
    mmr_k=50,
    mmr_diversity_bias=0.3,
)
response = query_engine.query(query)
print(response)

query_engine = index.as_query_engine(
    similarity_top_k=5,
    summary_enabled=False,
)
response = query_engine.query(query)
print(response)
