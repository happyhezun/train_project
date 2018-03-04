#encoding:utf-8
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
	return '这里是知了课堂。欢迎来到这里学习。'

if __name__ == '__main__':
	app.run()