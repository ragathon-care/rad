import os
from multiprocessing import Pool
import download_utils  # This is the new module where your function is
import pandas as pd 
pdf_url_df = pd.read_pickle('pdf_url_df.pkl')

pdf_urls = list(pdf_url_df.child_url.unique())
output_directory = 'downloaded_pdfs_multi3'
os.makedirs(output_directory, exist_ok=True)

def download_pdfs_concurrently(pdf_urls):
    with Pool() as pool:
        results = pool.starmap(download_utils.download_pdf, [(url, output_directory) for url in pdf_urls])

if __name__ == "__main__":
    pdf_name_mapping = download_pdfs_concurrently(pdf_urls)
    # for url, pdf_name in pdf_name_mapping.items():
    #     print(f"Downloaded {pdf_name} from {url}")
    # with open('pdf_name_mapping.txt', 'w') as mapping_file:
    #     for url, pdf_name in pdf_name_mapping.items():
    #         mapping_file.write(f"{url}: {pdf_name}\n")
