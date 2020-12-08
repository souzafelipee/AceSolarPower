from engine import Base
from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from apps.models.TiposInversorEnum import TiposInversorEnum
from apps.models.TiposEstruturaEnum import TiposEstruturaEnum
from apps.models.TiposModuloEnum import TiposModuloEnum
from .KitProduto import KitProduto


class Kit(Base):
    __tablename__ = 'kit'
    codKit = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    precoVenda = Column(Float)
    qtdeModulos = Column(Integer)
    potenciaModulo = Column(Float)
    tipoModulo = Column(Enum(TiposModuloEnum))
    marcaModulo = Column(String)
    descricaoModulo = Column(String)
    qtdeInversor = Column(Integer)
    potenciaInversor = Column(Float)
    tipoInversor = Column(Enum(TiposInversorEnum))
    marcaInversor = Column(String)
    descricaoInversor = Column(String)
    tipoEstrutura = Column(Enum(TiposEstruturaEnum))
    descricaoCompleta = Column(String)
    produtos = relationship("KitProduto")



