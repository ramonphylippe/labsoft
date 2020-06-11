from jwt import DecodeError
from rest_framework_jwt.utils import jwt_decode_handler


def getInfoFromToken(token):
    decode_payload = jwt_decode_handler(token)
    user_id = decode_payload.get('user_id')
    username = decode_payload.get('username')
    email = decode_payload.get('email')
    print(user_id, username, email)


def checkTokenValidation(token):
    try:
        jwt_decode_handler(token)
        return bool(True)
    except DecodeError:
        return bool(False)


def getIdFromToken(token):
    try:
        decode_payload = jwt_decode_handler(token)
        user_id = decode_payload.get('user_id')
        return user_id
    except DecodeError:
        print("tentativa de acesso com token invalido")
        return None
