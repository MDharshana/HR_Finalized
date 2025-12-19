from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


print(os.getenv("DATABASE_URL"))
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,        # reduce for Supabase
    max_overflow=2,
    connect_args={"sslmode": "require"},
)

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set in environment")


engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()    

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()