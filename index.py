import hashlib
import string
from hashlib import md5

from flask import Flask, render_template, url_for
from flask import request
from flask import make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql
import numpy as np
pymysql.install_as_MySQLdb()


app = Flask(__name__, static_url_path='')

# 提供一个返回页面的接口 路径可以自己定义


@app.route("/index",methods=['POST', 'GET'])
def index():

    return app.send_static_file('index.html')


# 提供一个返回页面的接口 路径可以自己定义
@app.route("/login",methods=['POST', 'GET'])
def login():

    return app.send_static_file('login.html')


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@113.116.75.60:3306/note"
db = SQLAlchemy(app)


def op_mysql(sql:string):
        results = '执行成功'
        # 打开数据库连接
        db = pymysql.connect(host='113.116.75.60',
                             user='root',
                             password='root',
                             database='note')

        # 使用cursor()方法获取操作游标
        # 建立游标
        cursor = db.cursor(pymysql.cursors.DictCursor)

        # 执行SQL语句
        cursor.execute(sql)
        db.commit()

        if sql.strip().lower().startswith('select'):
            # 获取所有记录列表
            results = cursor.fetchall()
        # 关闭数据库连接
            cursor.close()
            db.close()

            return results

# 加密


def md5(s, sqlt='$!@#$12232'):
    s=(str(s)+sqlt).encode()
    m=hashlib.md5(s)
    return m.hexdigest()


@app.route("/api/register", methods=['POST', 'GET'])
def register():
    # 第一步拿到接受到的参数
    # 这么访问对象的值比较好
    # print(datas['name'])
    datas = request.json
    if  datas['name'] and datas['password'] and datas['cpassword']:

        if datas['name']!=None:
            if datas['password']==datas['cpassword']:

                sql="select *  from  user_info  where name='%s';" % datas['name']

                if op_mysql(sql):
                     print("用户已存在")
                     return {
                         "status": False,
                         "msg": "用户已存在"
                     }

                else:
                    md5_pwd=md5(datas['password'])

                    sql12="INSERT INTO  user_info (name,phone,password ) VALUES ('%s','%s','%s');" % (datas['name'],datas['phone'],md5_pwd)

                    op_mysql(sql12)

                    print("注册成功")

                    return {
                        "status": True,
                        "msg": "注册成功"
                    }
            else:
                print('两次密码输入不正确')
                return {
                    "status": False,
                    "msg": "密码输入不正确"
                }
        else:
            print('用户名不能为空')
            return {
                "status": False,
                "msg": "用户名不能为空"
            }


@app.route("/api/login", methods=['POST', 'GET'])
def login_page():
        # 获取前端的参数
        datas=request.json
        # 先查找用没有这个用户名存在
        sql = "select * from user_info where name='{0}';" .format(datas['name'])
        # 这里面包括了执行sql语句
        res=op_mysql(sql)
        # 如果成立
        if res:
            # 都写下注释，我看不太懂。！0.0
            #
            # 就执行这条sql命令
            md5_pwd = md5(datas['password'])
            sql = "select * from user_info where name='{0}' and password='{1}';".format(datas['name'], md5_pwd)

            res1=op_mysql(sql)
            # 如果找相应的用户名和密码
            if res1 :
                # 登录成功
                print('用户%s登录成功'%datas['name'])
                return {
                    "status": True,
                    "msg": "用户登录成功"
                }
            else:
                print('密码错误')

                return {
                    "status":False,
                    "msg":"用户密码错误"
                }
        else:
            print("用户名%s不存在"%datas['name'])
            return {
                "status": False,
                "msg": "用户不存在"
            }



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