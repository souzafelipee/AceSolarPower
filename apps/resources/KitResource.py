from flask import request
from flask_restful import Resource
from apps.schemas.kitSchema import KitSchema
from marshmallow import ValidationError
from apps.responses import *
from dao import Session
from apps.models.Kit import Kit


class CadastrarKit(Resource):
    def post(self, *args, **kwargs):
        req = request.get_json() or None
        schema = KitSchema()
        try:
            novoKit = schema.load(req)
        except ValidationError as e:
            return resp_exception('Kit', description=str(e.messages))
        except Exception as e:
            return resp_exception('Kit', description=str(e))
        session = Session()
        session.add(novoKit)
        session.commit()
        result = schema.dump(novoKit)
        # Retorno 200 o meu endpoint
        return resp_ok(
            'Kit', 'Kit cadastrado com sucesso', data=result,
        )

    def get(self):
        session = Session()
        kits = session.query(Kit).all()
        schema = KitSchema(many=True)
        result = schema.dump(kits)
        return result


class ObterKitPorNome(Resource):
    def get(self, nomeKit):
        session = Session()
        query = session.query(Kit).filter(Kit.nome.ilike('%'+nomeKit+'%'))
        kits = query.all()
        schema = KitSchema(many=True)
        result = schema.dump(kits)
        return result


class ObterKit(Resource):
    def get(self, codKit):
        session = Session()
        query = session.query(Kit).filter(Kit.codKit == codKit)
        kit = query.one()
        schema = KitSchema()
        result = schema.dump(kit)
        return result

    def post(self, codKit):
        req = request.get_json() or None
        schema = KitSchema()
        try:
            kitAtualizado = schema.load(req)
        except ValidationError as e:
            return resp_exception('Kit', description=str(e.messages))
        except Exception as e:
            return resp_exception('Kit', description=str(e))
        session = Session()
        session.query(Kit).filter(Kit.codKit == codKit).update(req, synchronize_session=False)
        session.commit()
        result = schema.dump(kitAtualizado)
        # Retorno 200 o meu endpoint
        return resp_ok(
            'Kit', 'Kit atualizado com sucesso', data=result,
        )


