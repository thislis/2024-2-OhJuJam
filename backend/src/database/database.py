from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "'sqlite://OhJuJam.db"

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()