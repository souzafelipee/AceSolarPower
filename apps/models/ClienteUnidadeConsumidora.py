from engine import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum
from apps.models.ClassesEnum import ClassesEnum
from apps.models.FasesEnum import FasesEnum


class ClienteUnidadeConsumidora(Base):
    __tablename__ = 'clienteunidadeconsumidora'
    codClienteUnidadeConsumidora = Column(Integer, primary_key=True)
    codCliente = Column(Integer, ForeignKey('cliente.codCliente'))
    numeroUC = Column(String, nullable=False)
    endereco = Column(String)
    numero = Column(String)
    codCidade = Column(Integer)
    bairro = Column(String)
    consumoMedioMensal = Column(Float)
    taxaDisponibilidade = Column(Float)
    classe = Column(Enum(ClassesEnum))
    fase = Column(Enum(FasesEnum))
    seq = Column(Integer)
