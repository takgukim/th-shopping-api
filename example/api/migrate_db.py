from sqlalchemy import create_engine

from example.api.models.task import Base

DB_URL = "mysql+pymysql://root:test@127.0.0.1:3306/th_shopping_db"
engine=create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()