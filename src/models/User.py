from datetime import datetime
from src.models.Task import Task
from src import db


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_task = db.relationship(Task, backref="user")
    is_admin = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return "User(username='{}', email={}, user_task={})".format(
            self.username,
            self.email,
            self.user_task
        )
