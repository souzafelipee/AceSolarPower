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
        print(req)
        schema = ClienteSchema()
        try:
            novoCliente = schema.load(req)
            print(novoCliente)
        except ValidationError as e:
            print('erro de validação')
            return resp_exception('Cliente', description=str(e.messages))
        except Exception as e:
            print('exception normal')
            return resp_exception('Cliente', description=str(e))
        session = Session()
        session.add(novoCliente)
        session.commit()
        result = schema.dump(novoCliente)
        # Retorno 200 o meu endpoint
        return resp_ok(
            'Cliente', 'Cliente cadastrado com sucesso', data=result,
        )

    def get(self):
        session = Session()
        clientes = session.query(Cliente).all()
        schema = ClienteSchema(many=True)
        result = schema.dump(clientes)
        return result


class ObterClientesPorNome(Resource):
    def get(self, nomeCliente):
        session = Session()
        query = session.query(Cliente).filter(Cliente.nome.ilike('%'+nomeCliente+'%'))
        cliente = query.all()
        schema = ClienteSchema(many=True)
        result = schema.dump(cliente)
        return result


class ObterCliente(Resource):
    def get(self, codCliente):
        session = Session()
        query = session.query(Cliente).filter(Cliente.codCliente == codCliente)
        cliente = query.one()
        schema = ClienteSchema()
        result = schema.dump(cliente)
        return result

    def post(self, codCliente):
        req = request.get_json() or None
        print(req)
        schema = ClienteSchema()
        try:
            clienteAtualizado = schema.load(req)
        except ValidationError as e:
            return resp_exception('Cliente', description=str(e.messages))
        except Exception as e:
            return resp_exception('Cliente', description=str(e))
        session = Session()
        session.query(Cliente).filter(Cliente.codCliente == codCliente).update(clienteAtualizado)
        session.commit()
        result = schema.dump(clienteAtualizado)
        # Retorno 200 o meu endpoint
        return resp_ok(
            'Cliente', 'Cliente atualizado com sucesso', data=result,
        )




