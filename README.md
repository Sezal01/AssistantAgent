Overview
The Insight Assistant Agent is a chatbot that provides data insights using the RAG (Retrieval-Augmented Generation) model. It exposes APIs to query invoice-related data from a PostgreSQL database and returns insights via natural language, utilizing OpenAI for NLP and Pinecone for vector search.
Technologies
FastAPI: API framework.
OpenAI API: For NLP responses.
Pinecone: Vector database for search.
PostgreSQL: Relational DB for invoice data.
SQLAlchemy: ORM for PostgreSQL.
Docker: For containerization.

Setup
Clone repo:
git clone <repo-url>

Install dependencies:
pip install -r requirements.txt

Set up PostgreSQL and create tables for invoices.

Configure API keys


Setup
Clone repo:
git clone <repo-url>

Install dependencies:
pip install -r requirements.txt

Set up PostgreSQL and create tables for invoices.

Configure API keys in .env.
