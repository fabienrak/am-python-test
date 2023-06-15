from datetime import datetime
from src import db


class Task(db.Model):
    __tablename__ = "task"

    task_id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(255), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    task_author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    is_completed = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return 'Task>>> {self.task_title}'
