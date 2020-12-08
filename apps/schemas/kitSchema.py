from marshmallow import Schema
from marshmallow.fields import Str, Int, Float
from marshmallow import post_load
from marshmallow_enum import EnumField
from apps.models.Kit import Kit
from apps.messages import MSG_FIELD_REQUIRED
from apps.models.TiposModuloEnum import TiposModuloEnum
from apps.models.TiposEstruturaEnum import TiposEstruturaEnum
from apps.models.TiposInversorEnum import TiposInversorEnum


class KitSchema(Schema):
    codKit = Int()
    nome = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    precoVenda = Float(allow_none=True)
    qtdeModulos = Int(allow_none=True)
    potenciaModulo = Float(allow_none=True)
    tipoModulo = EnumField(TiposModuloEnum, by_value=True, allow_none=True)
    marcaModulo = Str(allow_none=True)
    descricaoModulo = Str(allow_none=True)
    qtdeInversor = Str(allow_none=True)
    potenciaInversor = Float(allow_none=True)
    tipoInversor = EnumField(TiposInversorEnum, by_value=True, allow_none=True)
    marcaInversor = Str(allow_none=True)
    descricaoInversor = Str(allow_none=True)
    tipoEstrutura = EnumField(TiposEstruturaEnum, by_value=True, allow_none=True)
    descricaoCompleta = Str(allow_none=True)

    @post_load
    def make_kit(self, data, **kwargs):
        return Kit(**data)



