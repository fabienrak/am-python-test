import json
import sys
from flasgger import swag_from
from flask import Blueprint, request, jsonify, make_response

from src.models.User import User
from src.models.Task import Task
from src import db
from src.utils.utils import auth_required, success_response, error_response

task_blueprint = Blueprint('TaskRoute', __name__, url_prefix="/task")


@task_blueprint.route('/all_task', methods=['GET'])
@auth_required
@swag_from('../docs/task/all_task.yaml')
def get_all_task(user_connected):
    try:
        all_task = Task.query.filter_by(task_author_id=user_connected).all()

        task_data = []
        if not all_task:
            return make_response(jsonify({
                'message': 'Erreur de recuperation des task'
            }))
        for task in all_task:
            task_data.append({
                'task_id': task.task_id,
                'task_title': task.task_title,
                'task_description': task.task_description,
                'task_author_id': task.task_author_id,
                'created_at': task.created_at
            })

        return success_response(task_data)
    except Exception as e:
        return error_response(str(e))


@task_blueprint.route('/get_task/<task_id>', methods=['GET'])
@auth_required
@swag_from('../docs/task/get_task_by_id.yaml')
def get_task_by_id(user_connected, task_id):
    task = Task.query.filter_by(task_id=task_id, task_author_id=user_connected).first()
    if not task:
        return jsonify({'message': 'AUCUNE TASK CORRESPONDANT'})
    else:
        try:
            task_data = {
                'task_id': task.task_id,
                'task_title': task.task_title,
                'task_description': task.task_description,
                'task_author_id': task.task_author_id,
                'created_at': task.created_at
            }
            return success_response(task_data)
        except Exception as e:
            return error_response(str(e))


@task_blueprint.route('/get_task', methods=['POST'])
@auth_required
@swag_from('../docs/task/get_task_by_name.yaml')
def get_task_by_name(user_connected):
    task_name = request.json.get('task_name')

    task = Task.query.filter_by(task_title=task_name, task_author_id=user_connected).first()
    if not task:
        return error_response('AUCUNE TASK CORRESPONDANT')
    else:
        task_data = {
            'task_id': task.task_id,
            'task_title': task.task_title,
            'task_description': task.task_description,
            'task_author_id': task.task_author_id,
            'created_at': task.created_at
        }
        return success_response(task_data)


@task_blueprint.route('/add_task', methods=['POST'])
@auth_required
@swag_from('../docs/task/add_task.yaml')
def add_task(user_connected):
    task_data = request.get_json()
    task_existed = Task.query.filter_by(task_title=task_data['task_title']).first()
    if task_existed:
        return error_response('TASK DEJA AJOUTER')
    else:
        try:
            new_task = Task(
                task_title=task_data['task_title'],
                task_description=task_data['task_description'],
                is_completed=False,
                task_author_id=user_connected,
            )
            db.session.add(new_task)
            db.session.commit()

            return success_response('TASK AJOUTER AVEC SUCCESS')
        except Exception as e:
            return error_response(str(e))


@task_blueprint.route('/edit_task', methods=['GET'])
def edit_task():
    return jsonify({
        "message": "EDIT TASK"
    })


@task_blueprint.route('/delete_task/<task_id>', methods=['DELETE'])
@auth_required
@swag_from('../docs/task/delete_task.yaml')
def delete_task(user_connected, task_id):
    task = Task.query.filter_by(task_id=task_id, user_id=user_connected).first()
    if not task:
        return success_response('AUCUNE TASK CORRESPONDANT')
    else:
        try:
            db.session.delete(task)
            db.session.commit()
            return success_response('TASK SUPPRIMER')
        except Exception as e:
            return error_response(str(e))


@task_blueprint.route('/complete_task/<task_id>', methods=['PUT'])
@auth_required
def complete_task(user_connected, task_id):
    task = Task.query.filter_by(task_id=task_id, user_id=user_connected).first()
    if not task:
        return error_response('AUCUNE TASK CORRESPONDANT')
    else:
        try:
            task.is_completed = True
            db.session.commit()
            return success_response('TASK FINI')
        except Exception as e:
            return error_response(str(e))
