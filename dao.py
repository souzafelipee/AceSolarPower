from engine import (Base, engine)
from sqlalchemy.orm import sessionmaker
from apps.models.Cliente import Cliente

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)



