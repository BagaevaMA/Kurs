import sqlalchemy
from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://postgres:a3262626i@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

session.close()