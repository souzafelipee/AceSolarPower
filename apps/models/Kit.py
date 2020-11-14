from engine import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .KitProduto import KitProduto

class Kit(Base):
    __tablename__ = 'kit'
    codKit = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    valorTotal= Column(Float)
    produtos = relationship("KitProduto")



