from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from apps.models.Produto import Produto
from apps.schemas.produtoSchema import ProdutoSchema
from dao import Session
from apps.responses import *


class CadastrarProduto(Resource):
    def post(self, *args, **kwargs):
        req = request.get_json() or None
        schema = ProdutoSchema()
        try:
            novoProduto = schema.load(req)
        except ValidationError as e:
            return resp_exception('Cliente', description=str(e.messages))
        except Exception as e:
            return resp_exception('Cliente', description=str(e))
        session = Session()
        session.add(novoProduto)
        session.commit()
        result = schema.dump(novoProduto)
        # Retorno 200 o meu endpoint
        return resp_ok(
            'Produto', 'Produto cadastrado com sucesso', data=result,
        )

    def get(self):
        session = Session()
        produtos = session.query(Produto).all()
        schema = ProdutoSchema(many=True)
        result = schema.dump(produtos)
        return result


class ObterProdutosPorNome(Resource):
    def get(self, nomeProduto):
        session = Session()
        query = session.query(Produto).filter(Produto.nome.ilike('%'+nomeProduto+'%'))
        produtos = query.all()
        schema = ProdutoSchema(many=True)
        result = schema.dump(produtos)
        return result


class ObterProduto(Resource):
    def get(self, codProduto):
        session = Session()
        query = session.query(Produto).filter(Produto.codProduto == codProduto)
        produto = query.one()
        schema = ProdutoSchema()
        result = schema.dump(produto)
        return result

    def post(self, codProduto):
        req = request.get_json() or None
        schema = ProdutoSchema()
        try:
            produtoAtualizado = schema.load(req)
        except ValidationError as e:
            return resp_exception('Produto', description=str(e.messages))
        except Exception as e:
            return resp_exception('Produto', description=str(e))
        session = Session()
        session.query(Produto).filter(Produto.codProduto == codProduto).update(req, synchronize_session=False)
        session.commit()
        result = schema.dump(produtoAtualizado)
        # Retorno 200 o meu endpoint
        return resp_ok(
            'Produto', 'Produto atualizado com sucesso', data=result,
        )




