# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Aritcle(db.Model):
    __tablename__ = 'aritcle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.forgnkey('user.id'))
    author = db.relationship('user', backref=db.backref('aritcle'))


db.create_all()


@app.route('/')
def index():
    return 'Hello, World!!'


@app.route('/test')
def test():
	return 'test url'


if __name__ == '__main__':
    app.run()
