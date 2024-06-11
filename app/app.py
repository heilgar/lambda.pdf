import os
from openai import OpenAI


import pypdf
import camelot
import pandas as pd
import pdfplumber
import fitz  # PyMuPDF
import requests


# client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def handler(event, context):
    # # Example usage of openai
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "Say this is a test",
    #         }
    #     ],
    #     model="gpt-3.5-turbo"
    # )
    # print(chat_completion)

    pdf_file_path = os.getenv('PDF_FILE_PATH', '/tmp/sample.pdf')

    # # Example usage of PyPDF2
    with open(pdf_file_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        page = reader.pages[0]
        text = page.extract_text()
        print("!!!! PyPDF2 Extracted Text:\n", text)

    # # Example usage of camelot
    tables = camelot.read_pdf(pdf_file_path)
    print("!!!! Camelot Tables:\n", tables[0].df)

    # # Example usage of pandas
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("!!!! Pandas DataFrame:\n", df)

    # # Example usage of pdfplumber
    with pdfplumber.open(pdf_file_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        print("!!!! pdfplumber Extracted Text:\n", text)

    # # Example usage of PyMuPDF
    doc = fitz.open(pdf_file_path)
    page = doc.load_page(0)
    text = page.get_text("text")
    print("PyMuPDF Extracted Text:\n", text)

    # # Example usage of requests
    response = requests.get('https://swapi.dev/api/people/1/')
    print("!!!! Requests Response:", response.json())

    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully!',
    }

if __name__ == '__main__':
    handler(None, None)