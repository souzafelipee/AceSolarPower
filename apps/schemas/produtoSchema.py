from marshmallow import Schema
from marshmallow.fields import Str, Int, Float
from marshmallow import post_load
from marshmallow_enum import EnumField
from apps.models.Produto import Produto
from apps.messages import MSG_FIELD_REQUIRED
from apps.models.TiposProdutoEnum import TiposProdutoEnum
from apps.models.TiposModuloEnum import TiposModuloEnum
from apps.models.TiposEstruturaEnum import TiposEstruturaEnum
from apps.models.TiposInversorEnum import TiposInversorEnum


class ProdutoSchema(Schema):
    codProduto = Int()
    nome = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    marca = Str()
    potencia = Float()
    custoMedioMensal = Float()
    custoUltimaCompra = Float()
    tipoProduto = EnumField(TiposProdutoEnum, by_value=True)
    tipoModulo = EnumField(TiposModuloEnum, by_value=True)
    tipoInversor = EnumField(TiposInversorEnum, by_value=True)
    tipoEstrutura = EnumField(TiposEstruturaEnum, by_value=True)

    @post_load
    def make_produto(self, data, **kwargs):
        return Produto(**data)

