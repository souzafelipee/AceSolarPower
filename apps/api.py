# Importamos as classes API e Resource
from flask_restful import Api, Resource
from apps.resources.ClienteResource import CadastrarCliente, ObterCliente, ObterClientesPorNome
from apps.resources.ProdutoResource import CadastrarProduto, ObterProduto, ObterProdutosPorNome


# Criamos uma classe que extende de Resource
class Index(Resource):
    def get(self):
        return {'status': 'O servidor esta ON! HIKEN!'}


# Instânciamos a API do FlaskRestful
api = Api()


def configure_api(app):
    # adicionamos na rota '/' a sua classe correspondente Index
    api.add_resource(Index, '/')
    api.add_resource(CadastrarCliente, '/cliente')
    api.add_resource(ObterCliente, '/cliente/<int:codCliente>')
    api.add_resource(ObterClientesPorNome, '/cliente/nome/<string:nomeCliente>')
    api.add_resource(CadastrarProduto, '/produto')
    api.add_resource(ObterProduto, '/produto/<int:codProduto>')
    api.add_resource(ObterProdutosPorNome, '/produto/nome/<string:nomeProduto>')


    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)

