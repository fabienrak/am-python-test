from flasgger import swag_from
from flask import jsonify, Blueprint, request
from flask_bcrypt import generate_password_hash, check_password_hash
from src.utils.utils import generate_token, auth_required
from src.models.User import User
from src import db
import validators

auth_blueprint = Blueprint("auth_user", __name__, url_prefix="/auth")


@auth_blueprint.route('/signup', methods=['POST'])
@swag_from('../docs/auth/auth_register.yaml')
def user_register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    try:
        if len(password) < 6:
            return jsonify({'error': "MOT DE PASSE DOIT CONTENIR 6 CARACTERE AU MOINS"}), 400

        if len(username) < 3:
            return jsonify({'error': "NOM D UTILISATEUR DOIT CONTENIR 6 CARACTERE AU MOINS"}), 400

        if not username.isalnum() or " " in username:
            return jsonify({'error': "LE NOM D UTILISATEUR NE DOIT PAS CONTENIR DES CARACTERES SPECIAUX"}), 400

        if not validators.email(email):
            return jsonify({'error': "FORMAT EMAIL NON VALIDE"}), 400

        if User.query.filter_by(email=email).first() is not None:
            return jsonify({'error': "EMAIL DEJA UTILISE"}), 409

        if User.query.filter_by(username=username).first() is not None:
            return jsonify({'error': "NOM D UTILISATEUR DEJA UTILISER"}), 409

        password_hash = generate_password_hash(password).decode('utf8')
        new_user = User(username=username, password=password_hash, email=email, is_admin=False)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'message': "UTILISATEUR INSCRIT AVEC SUCCESS",
            'user': {
                'username': username, "email": email
            }
        }), 201
    except Exception as e:
        return jsonify({
            'message': str(e)
        }), 500


@auth_blueprint.route('/signin', methods=['POST'])
@swag_from('../docs/auth/auth_login.yaml')
def user_login():

    email = request.json.get('email', '')
    password = request.json.get('password', '')

    app_user = User.query.filter_by(email=email).first()

    if app_user:
        check_correct_pwd = check_password_hash(app_user.password, password)
        if check_correct_pwd:
            token = generate_token(payload=request.get_json(), dureeToken=60)
            return jsonify({
                'message': "UTILISATEUR CONNECTE AVEC SUCCESS",
                'token': token,
                'email': email,
            }), 200
        else:
            return jsonify({
                'message': "MOT DE PASSE INCORRECT"
            }), 401


@auth_blueprint.route('/add_admin/<user_id>', methods=['POST'])
def set_admin_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({
            'message': 'AUCUN UTILISATEUR CORRESPONDANT'
        })
    user.is_admin = True
    db.session.commit()
    return jsonify({
        'message': 'STATUS CHANGE EN ADMINISTRATEUR'
    })

@auth_blueprint.route('/all_user', methods=['GET'])
@auth_required
def get_all_users(user_connected):
    if not user_connected.is_admin:
        return jsonify({
            'message':'ACCESS REFUSER'
        })
    user = User.query.all()
    all_user = []
    for usr in user:
        user_data = {
            'username': usr.username,
            'email': usr.email
        }
        all_user.append(user_data)
        return jsonify({
            'message':all_user
        })
