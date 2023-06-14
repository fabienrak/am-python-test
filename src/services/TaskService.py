import json

from flasgger import swag_from
from flask import Blueprint, request, jsonify
from src.models.Task import Task
from src import db
from src.utils.utils import auth_required, success_response

task_blueprint = Blueprint('TaskRoute', __name__, url_prefix="/task")


@task_blueprint.route('/all_task', methods=['GET'])
@auth_required
@swag_from('../docs/task/all_task.yaml')
def get_all_task(user_connected):
    all_task = Task.query.filter_by(user_id=user_connected.user_id).all()
    #task_data = []

    for task in all_task:
        all_task_data = [{
            'task_id': task.task_id,
            'task_title': task.task_title,
            'task_description': task.task_description,
            'task_author_id': task.task_author_id,
            'created_at': task.created_at
        }]
        #task_data.append(all_task_data)

    return jsonify({'data':all_task_data}), 200


@task_blueprint.route('/get_task/<task_id>', methods=['GET'])
@auth_required
def get_task_by_id(user_connected, task_id):
    task = Task.query.filter_by(task_id=task_id, user_id=user_connected.user_id).first()
    if not task:
        return jsonify({'message': 'AUCUNE TASK CORRESPONDANT'})
    task_data = {
        'task_id': task.task_id,
        'task_title': task.task_title,
        'task_description': task.task_description,
        'task_author_id': task.task_author_id,
        'created_at': task.created_at
    }
    return jsonify(json.load(task_data))


@task_blueprint.route('/add_task', methods=['POST'])
@auth_required
def add_task(user_connected):
    task_data = request.get_json()
    new_task = Task(
        task_title=task_data['task_title'],
        task_description=task_data['task_description'],
        task_author_id=user_connected.user_id,
        is_completed=False
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "message": "TASK AJOUTER AVEC SUCCESS",
    }), 201


@task_blueprint.route('/edit_task', methods=['GET'])
def edit_task():
    return jsonify({
        "message": "EDIT TASK"
    })


@task_blueprint.route('/delete_task/<task_id>', methods=['DELETE'])
@auth_required
def delete_task(user_connected, task_id):
    task = Task.query.filter_by(task_id=task_id, user_id=user_connected.user_id).first()
    if not task:
        return jsonify({
            "message": "AUCUNE TASK CORRESPONDANT"
        })
    db.session.delete(task)
    db.session.commit()
    return jsonify({
        'message': 'TASK SUPPRIMER !!'
    })


@task_blueprint.route('/complete_task/<task_id>', methods=['PUT'])
@auth_required
def complete_task(user_connected, task_id):
    task = Task.query.filter_by(task_id=task_id, user_id=user_connected.user_id).first()
    if not task:
        return jsonify({
            'message': 'AUCUNE TASK CORRESPONDANT'
        })
    task.is_completed = True
    db.session.commit()
    return jsonify({
        'message': 'TASK FINI !!'
    })
