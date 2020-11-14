from engine import (Base, engine)
from sqlalchemy.orm import sessionmaker
from apps.models.Cliente import Cliente
from apps.models.Kit import Kit
from apps.models.Produto import Produto

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)



