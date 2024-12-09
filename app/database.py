from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define SQLAlchemy models
class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True)
    invoice_amount = Column(Integer)
    status = Column(String)

# Create tables in the database (only once during setup)
Base.metadata.create_all(bind=engine)

# Get data for a specific project
def get_invoice_data(project_name: str):
    db = SessionLocal()
    return db.query(Invoice).filter(Invoice.project_name == project_name).all()

# Save data to the database
def save_invoice_data(data: dict):
    db = SessionLocal()
    new_invoice = Invoice(
        project_name=data['project_name'],
        invoice_amount=data['amount'],
        status=data['status']
    )
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
