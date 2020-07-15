from apps import db
from orm.model import User
from utils import MD5Util
from flask import Blueprint, request, make_response, jsonify
from sqlalchemy import or_, and_


# 创建一个蓝图，蓝图名称 user，前缀 /user
user_dp = Blueprint("user", __name__, url_prefix="/user")


# 后面写API接口 =============================================================


# 登录判断
@user_dp.route('/login', methods=["GET", "POST"])
def login():
    # 获取用户名和密码，并密码加密
    username = request.json['username']
    password = request.json['password']
    password = MD5Util.md5vale(password)

    # 将用户名和加密后的密码去数据库查询
    user = db.session.query(User).filter(and_(
        User.username == username,
        User.password == password
    )).first()

    result = {}
    if user is not None:  # 登录成功
        result["flag"] = True
        result["msg"] = "登录成功"
        result["data"] = user.to_json()
    else:   # 登录失败
        result["flag"] = False
        result["msg"] = "登录失败"

    # 解决前后端分离跨域问题
    rst = make_response(jsonify(result))
    rst.headers['Access-Control-Allow-Origin'] = '*'  # 任意域名
    if request.method == 'POST':
        rst.headers['Access-Control-Allow-Methods'] = 'POST'  # 响应POST
    return rst
