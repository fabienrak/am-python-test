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
        token = None
        if 'Authorization' in request.headers or 'x-access-token' in request.headers or 'token' in request.json:
            token = request.headers.get(
                'x-access-token', None) or request.json.get('token', None) or request.headers.get('Authorization')
            token = token.replace('Bearer ', '')
        else:
            return jsonify({'message': 'TOKEN REQUIS'})
        try:
            decoded = decode_jwt(token)
            user = User.query.filter_by(email=decoded['email']).first()
            user_connected = User.query.filter_by(user_id=user.user_id).first()
            if not user:
                return jsonify({'message': 'UTILISATEUR NON TROUVER !! '})
        except:
            return jsonify({'message': 'INVALIDE TOKEN !! '})
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
