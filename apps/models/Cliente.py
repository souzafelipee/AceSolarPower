from engine import Base
from sqlalchemy import Column, Integer, String


class Cliente(Base):
    __tablename__ = 'cliente'
    codCliente = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cnpjCpf = Column(String, nullable=False)
    celular = Column(String)
    email = Column(String)

    #def __repr__(self):
        #return "<Cliente(nome={self.nome!r}, cnpjCpf={self.nome!r})>".format(self=self)
