from engine import Base
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .Produto import Produto


class KitProduto(Base):
    __tablename__ = 'kitproduto'
    codKitProduto = Column(Integer, primary_key=True)
    codKit = Column(Integer, ForeignKey('kit.codKit'))
    codProduto = Column(Integer, ForeignKey('produto.codProduto'))
    quantidade = Column(Float, nullable=False)
    valorUnitario = Column(Float, nullable=False)
    valorTotal = Column(Float)
    produto = relationship("Produto")



