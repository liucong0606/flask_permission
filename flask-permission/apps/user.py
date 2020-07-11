from apps import db
from utils import MD5Util
from flask import Blueprint, request, make_response, jsonify
from sqlalchemy import or_, and_


# 创建一个蓝图，蓝图名称 user，前缀 /user
user_dp = Blueprint("user", __name__, url_prefix="/user")


# 用户表
class User(db.Model):
    # 定义表名
    __tablename__ = 'tab_user'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    # 用户编号
    username = db.Column(db.String(32))     # 用户名
    password = db.Column(db.String(32))     # 密码
    gender = db.Column(db.String(32))       # 性别
    birthday = db.Column(db.Date)           # 生日
    remark = db.Column(db.String(32))       # 备注

    # 将数据转换成 json 格式
    def to_json(self):
        data_json = {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "gender": self.gender,
            "birthday": self.birthday,
            "remark": self.remark
        }
        return data_json


# 后面写API接口 =============================================================


# 登录判断
@user_dp.route('/login', methods=["GET", "POST"])
def login():
    # 获取用户名和密码，并密码加密
    username = request.json['username']
    password = request.json['password']
    password = MD5Util.md5vale(password)

    # 将用户名和加密后的密码去数据库查询
    users = db.session.query(User).filter(and_(
        User.username == username,
        User.password == password
    )).all()

    result = {}
    if len(users) > 0:  # 登录成功
        result["flag"] = True
        result["msg"] = "登录成功"
    else:   # 登录失败
        result["flag"] = False
        result["msg"] = "登录失败"

    # 解决前后端分离跨域问题
    rst = make_response(jsonify(result))
    rst.headers['Access-Control-Allow-Origin'] = '*'  # 任意域名
    if request.method == 'POST':
        rst.headers['Access-Control-Allow-Methods'] = 'POST'  # 响应POST
    return rst

