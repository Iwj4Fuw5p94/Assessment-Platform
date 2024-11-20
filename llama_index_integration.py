# llama_index_integration.py
from llama_index import VectorStoreIndex, SimpleDirectoryReader
 
# Initialize the document reader and index
documents = SimpleDirectoryReader("data/").load_data()  # Assuming questions are stored in files
index = VectorStoreIndex.from_documents(documents)
 
# Query the index
def query_index(query: str):
    response = index.query(query)
    return response
 
# Test the query
if __name__ == "__main__":
    query = "Tell me about AI assessments."
    result = query_index(query)
    print(f"Query Result: {result}")
    
# CLI OUTPUT:
# Query Result: AI assessments are an effective way to evaluate the skills of candidates using automated tools. These assessments often use machine learning algorithms to analyze responses...