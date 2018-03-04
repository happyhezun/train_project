#encoding:utf-8
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	login_url = url_for('login')
	return redirect(login_url)
	# return '这里是知了课堂。欢迎来到这里学习。'

@app.route('/login/')
def login():
	return '这是首页。'

if __name__ == '__main__':
	app.run(debug=True)