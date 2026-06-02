from sqlmodel import SQLModel, create_engine, Session
from app.models import Reading, Event
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./weather.db")

# Create engine
engine = create_engine(
    DATABASE_URL, 
    echo=False, 
    connect_args={"check_same_thread": False}
)

def create_db_and_tables():
    """Create all tables in the database"""
    SQLModel.metadata.create_all(engine)
    print("✅ Database tables created successfully!")

def get_session():
    """Dependency for FastAPI to get database session"""
    with Session(engine) as session:
        yield session