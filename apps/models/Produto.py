from engine import Base
from sqlalchemy import Column, Integer, String, Float, Enum
from apps.models.TiposProdutoEnum import TiposProdutoEnum
from apps.models.TiposInversorEnum import TiposInversorEnum
from apps.models.TiposEstruturaEnum import TiposEstruturaEnum
from apps.models.TiposModuloEnum import TiposModuloEnum


class Produto(Base):
    __tablename__ = 'produto'
    codProduto = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    marca = Column(String)
    potencia = Column(Float)
    custoMedioMensal = Column(Float)
    custoUltimaCompra = Column(Float)
    tipoProduto = Column(Enum(TiposProdutoEnum))
    tipoModulo = Column(Enum(TiposModuloEnum))
    tipoInversor = Column(Enum(TiposInversorEnum))
    tipoEstrutura = Column(Enum(TiposEstruturaEnum))



