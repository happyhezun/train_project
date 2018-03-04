#encoding:utf-8
from flask import Flask, render_template 
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
	# 返回页面内容
	content = u'''
	<h1>这个一个blog系统。</h1>
	'''
	# title = '首页'
	return render_template('index.html', title=content)

@app.route('/services')
def services():
	return 'Service'

@app.route('/about')
def about():
	return 'About'

@app.route('/user/<int:username>')
def user(username):
	return 'User %s' % username

if __name__ == '__main__':
	manager.run()
	# app.run(debug=True)
