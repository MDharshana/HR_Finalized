from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")  # Supabase Postgres URL

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

session = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()    

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()