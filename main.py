import os
import openai
import sys

sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


openai.api_key  = os.environ['OPENAI_API_KEY']


from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("text.pdf")
pages = loader.load()
page = pages[0]

# print(page.page_content)




