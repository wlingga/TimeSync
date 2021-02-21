from timesync import db, login_manager
from flask_login import UserMixin

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60))
    todos = db.relationship('Todo', backref='user', lazy="dynamic")

    def __repr__(self):
        return f"User('{self.username}', '{self.id}', '{self.email}')"\

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.String(100))
    end_time = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"Todo('{self.user_id}', '{self.title}', {self.start_time}', '{self.end_time}')"\

db.create_all()