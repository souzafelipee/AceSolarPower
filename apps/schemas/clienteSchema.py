from marshmallow import Schema
from marshmallow.fields import Str, Int, List, Nested
from marshmallow import post_load
from apps.models.Cliente import Cliente
from apps.messages import MSG_FIELD_REQUIRED
from .clienteUnidadeConsumidoraSchema import ClienteUnidadeConsumidoraSchema


class ClienteSchema(Schema):
    codCliente = Int()
    nome = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    cnpjCpf = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    celular = Str()
    email = Str()
    unidadesConsumidoras = List(Nested(ClienteUnidadeConsumidoraSchema))

    @post_load
    def make_cliente(self, data, **kwargs):
        return Cliente(**data)

