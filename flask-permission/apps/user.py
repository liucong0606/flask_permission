import apps
from flask import Blueprint


app = apps.get_app()    # 获取 本应用app对象
db = apps.db    # 获取数据库对象

# 创建一个蓝图，蓝图名称 user，前缀 /user
user_dp = Blueprint("user", __name__, url_prefix="/user")


# 用户表
class User(db.Model):
    pass
