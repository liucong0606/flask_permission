from flask import Blueprint, request, make_response, jsonify
from sqlalchemy import or_, and_
from apps import db
from orm.model import Role

# 创建一个蓝图，蓝图名称 role，前缀 /role
role_dp = Blueprint("role", __name__, url_prefix="/role")

# 后面写API接口 =============================================================
