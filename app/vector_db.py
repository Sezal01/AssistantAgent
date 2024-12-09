import pinecone

# Initialize Pinecone client
pinecone.init(api_key="your-pinecone-api-key", environment="us-west1-gcp")
index = pinecone.Index("invoice-index")

# Store data embeddings in the vector database
def store_embeddings(data: dict):
    vector = generate_vector_from_data(data)
    index.upsert([(str(data['invoice_id']), vector)])

# Query vector database
def query_embeddings(query: str):
    vector = generate_query_vector(query)
    results = index.query(vector, top_k=5)
    return results
