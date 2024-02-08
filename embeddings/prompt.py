from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory='emb',
    embedding_function=embeddings
)

retriever = db.as_retriever()  # for the Retrieval QA for managing the multuple databases, it maps with the relevent retrival method of the database.

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type='stuff' #this is a one of the simple chain type
    #other chain types are - refine, mapReduce,mapRerank
)

result = chain.invoke("Tell me interesting facts about the English")
print(result)


