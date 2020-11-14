from engine import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .ClienteUnidadeConsumidora import ClienteUnidadeConsumidora


class Cliente(Base):
    __tablename__ = 'cliente'
    codCliente = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cnpjCpf = Column(String, nullable=False)
    celular = Column(String)
    email = Column(String)
    unidadesConsumidoras = relationship("ClienteUnidadeConsumidora")

