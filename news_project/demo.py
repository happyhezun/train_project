# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/')
def index():
    # 插入数据到数据库
    # article = Article(title='aaa', content='bbb')
    # db.session.add(article)
    # db.session.commit()

    # 在数据库中查询数据
    # result = Article.query.filter(Article.title=='aaa').all()
    # for article in result:
    # 	print article.title, article.content

    # 修改数据步骤:
    # 1.先把需要修改的数据查询出来.
    # 2.把查询出来的数据修改.
    # article = Article.query.filter(Article.title=='aaa').first()
    # article.content = 'new title'
    # 保存数据
    # db.session.commit()

    # 删除数据
    # 1.先查询出需要删除的数据。
    # 2.删除数据。
    # article = Article.query.filter(Article.title=='aaa').first()
    # db.session.delete(article)
    # db.session.commit()

    return 'Hello, World!!'


if __name__ == '__main__':
    app.run()
