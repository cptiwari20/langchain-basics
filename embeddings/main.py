from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

# import the file and then split into chunks
# chunks should be in limited lenght and should be chunked based on line change
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0,
)

# Load the file 
loader = TextLoader("facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

db = Chroma.from_documents(
    docs,
    embedding_function=embeddings,
    persist_directory='emb'
)

result = db.similarity_search_with_score("What is english?")

print(result)
# for doc in docs:
#     print(doc.page_content)
#     print("\n")

# take those chunks and create embeddings
