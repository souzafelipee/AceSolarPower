from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from apps.models.Cliente import Cliente
from apps.schemas.clienteSchema import ClienteSchema
from dao import Session
from apps.responses import *


class CadastrarCliente(Resource):
    def post(self, *args, **kwargs):
        req = request.get_json() or None
        schema = ClienteSchema()
        novoCliente = ''

        try:
            novoCliente = schema.load(req)
        except ValidationError as e:
            return resp_exception('Cliente', description=str(e.messages))
        except Exception as e:
            return resp_exception('Cliente', description=str(e))
        session = Session()
        session.add(novoCliente)
        session.commit()
        result = schema.dump(novoCliente)
        # Retorno 200 o meu endpoint
        return resp_ok(
            'Cliente', 'Cliente cadastrado com sucesso', data=result,
        )


