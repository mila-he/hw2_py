from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Loo andmebaasi ühendus
DATABASE_URL = 'sqlite:///tvs.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Baasklass mudelite jaoks
Base = declarative_base()


# Tabelite loomine
def create_tables():
    Base.metadata.create_all(bind=engine)