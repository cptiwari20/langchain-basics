from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

# import the file and then split into chunks
# chunks should be in limited lenght and should be chunked based on line change
text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    keep_separator="/n"
)

# Load the file 
loader = TextLoader('facts.txt')
docs = loader.load_and_split(
    text_splitter=text_splitter
)

for doc in docs:
    print(doc)
    print("/n")

# take those chunks and create embeddings
