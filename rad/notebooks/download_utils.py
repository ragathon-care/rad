import os
import requests

def download_pdf(url, output_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            pdf_name = os.path.basename(url)
            pdf_path = os.path.join(output_directory, pdf_name)
            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(response.content)
            return url, pdf_name
        else:
            print(f"Failed to download PDF from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error while downloading {url}: {str(e)}")
