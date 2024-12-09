from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from .database import get_invoice_data, save_invoice_data
from .ai_integration import generate_insight
from .vector_db import store_embeddings, query_embeddings
from .security import validate_api_key
from .exceptions import handle_exception

app = FastAPI()

# Models for handling requests and responses
class InvoiceQuery(BaseModel):
    project_name: str
    query_type: str

class InsightResponse(BaseModel):
    insight: str

# Endpoint to upload invoice data (e.g., invoice JSON data)
@app.post("/data/upload")
async def upload_data(data: dict, api_key: str = Depends(validate_api_key)):
    try:
        # Save data to SQL or Vector Database
        save_invoice_data(data)
        return {"message": "Data uploaded successfully"}
    except Exception as e:
        handle_exception(e)
        raise HTTPException(status_code=500, detail="Error uploading data")

# Endpoint to query data (structured query using SQL)
@app.post("/data/query", response_model=InsightResponse)
async def query_data(query: InvoiceQuery, api_key: str = Depends(validate_api_key)):
    try:
        # Retrieve data from SQL Database
        invoice_data = get_invoice_data(query.project_name)
        
        # Generate insights using AI
        insight = generate_insight(invoice_data, query.query_type)
        return InsightResponse(insight=insight)
    except Exception as e:
        handle_exception(e)
        raise HTTPException(status_code=500, detail="Error generating insight")

# Endpoint to query vector database (e.g., Pinecone)
@app.get("/data/embedding-query")
async def embedding_query(query: str, api_key: str = Depends(validate_api_key)):
    try:
        results = query_embeddings(query)
        return {"results": results}
    except Exception as e:
        handle_exception(e)
        raise HTTPException(status_code=500, detail="Error querying vector database")
