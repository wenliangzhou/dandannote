from flask import Flask
from flask import request
from flask import make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql
import numpy as np
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@113.88.66.94:3306/note"
db = SQLAlchemy(app)


class user_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone
        }
url_for('static', filename='style.css')

@app.route("/api/register", methods=['POST', 'GET'])
def register():
    # 第一步拿到接受到的参数
    # print(request.form)
    print(request.query_string)
    print(request.headers.get('X-consumer-custom-id'))

    # 查询是否有此用户
    # db.session.add(user_info(name="zzz", phone="15072779728", password="123456"))
    # db.session.commit()
    # 如果没有则插入数据，有则提醒用户已注册。
    user = user_info.query.all()
    arr = []
    for item in user:
        arr.append({"id": item.id, "name": item.name, "phone": item.phone})
    context = {
        "data": arr
    }
    return make_response(context)


if __name__ == '__main__':
    app.run(port=8888, debug=True)