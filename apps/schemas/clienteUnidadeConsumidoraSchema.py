from marshmallow import Schema
from marshmallow.fields import Str, Int, Float
from marshmallow import post_load
from apps.models.ClienteUnidadeConsumidora import ClienteUnidadeConsumidora
from apps.messages import MSG_FIELD_REQUIRED


class ClienteUnidadeConsumidoraSchema(Schema):
    codClienteUnidadeConsumidora = Int()
    codCliente = Int()
    numeroUC = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    endereco = Str()
    numero = Str()
    codCidade = Int()
    bairro = Str()
    consumoMedioMensal = Float()
    taxaDisponibilidade = Float()
    classe = Str()
    fase = Str()
    seq = Int()

    @post_load
    def make_clienteUnidadeConsumidora(self, data, **kwargs):
        return ClienteUnidadeConsumidora(**data)

