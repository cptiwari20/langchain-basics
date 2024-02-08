from langchain.embeddings.base import Embeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import BaseRetriever

class RedundantFilterRetriever(BaseRetriever):
    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query):
        # calculate embeddings for the query string
        emb = self.embeddings.embed_query(query)
        #take embedding and feed it to the db with 
        # max_marginal_relevance_search_by_vector
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8 # 0-1 , to handle the relevance in this case.
        )
    
    async def aget_relevant_documents(self):
        return []