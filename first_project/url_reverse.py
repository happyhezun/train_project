#encoding:utf-8
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
	print url_for('my_list')
	print url_for('article', id='abc')
	return '这里是知了课堂。欢迎来到这里学习。'

@app.route('/list/')
def my_list():
	return 'list'

@app.route('/article/<id>')
def article(id):
	return u'你请求的参数是: %s' % id

if __name__ == '__main__':
	app.run(debug=True)