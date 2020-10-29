from flask import jsonify
from .messages import MSG_INVALID_DATA, MSG_DOES_NOT_EXIST, MSG_EXCEPTION
from .messages import MSG_ALREADY_EXISTS

def resp_exception(resource :str, description :str = '', msg :str = MSG_EXCEPTION):
    '''
    Responses 500
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')
    resp = jsonify({
        'resource': resource,
        'message': msg,
        'description': description
    })
    resp.status_code = 500
    return resp


def resp_ok(resource :str, message :str, data=None, **extras):
    '''
    Responses 200
    '''
    response = {'status': 200, 'message': message, 'resource': resource}
    if data:
        response['data'] = data
    response.update(extras)
    resp = jsonify(response)
    resp.status_code = 200
    return resp

