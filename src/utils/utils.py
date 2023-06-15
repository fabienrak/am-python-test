import os
from functools import wraps
import jwt
from datetime import datetime, timedelta
from flask import jsonify, request
from dotenv import load_dotenv
from src.models.User import User

load_dotenv()

'''
    Token Utils
'''


def generate_token(payload, dureeToken=None):
    if dureeToken:
        payload['exp'] = (datetime.now() + timedelta(minutes=dureeToken)).timestamp()
    return jwt.encode(payload, os.environ.get('JWT_SECRET_KEY'))


def decode_jwt(token):
    return jwt.decode(token, os.environ.get('JWT_SECRET_KEY'), algorithms=["HS256"])


def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'TOKEN REQUIS'}), 401
        else:
            token = token.replace('Bearer ', '')
        try:
            decoded = decode_jwt(token)
            user_connected = decoded['user_id']
        except Exception as e:
            return jsonify({'message': 'INVALIDE TOKEN !! ', 'data': str(e)})
        return f(user_connected, *args, **kwargs)
    return decorator


'''
    Response utils
'''


def success_response(msg):
    return jsonify({
        'data': msg,
        'success': True
    })


def error_response(msg):
    return jsonify({
        'data': msg,
        'success': False
    })
