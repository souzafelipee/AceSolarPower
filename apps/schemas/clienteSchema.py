from marshmallow import Schema
from marshmallow.fields import Str
from marshmallow import post_load
from apps.models.Cliente import Cliente
from apps.messages import MSG_FIELD_REQUIRED


class ClienteSchema(Schema):
    nome = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    cnpjCpf = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    celular = Str()
    email = Str()

    @post_load
    def make_cliente(self, data, **kwargs):
        return Cliente(**data)
