from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

dbString = getenv('DATABASE_URL')
print(dbString)
engine = create_engine(dbString, echo=True)
Base = declarative_base()

