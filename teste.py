from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String)

dbString = 'postgresql://postgres:masterkey@localhost/aefsolar'
engine = create_engine(dbString, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    codCliente = Column(Integer, primary_key=True)
    nome = Column(String)
    cnpjCpf = Column(String)
    celular = Column(String)
    email = Column(String)



Base.metadata.create_all(engine)
p1 = Cliente(nome='Felipe', cnpjCpf='03406769144')
p2 = Cliente(nome='Abner')

#session.add(p1)
session.add(p1)
session.commit()


