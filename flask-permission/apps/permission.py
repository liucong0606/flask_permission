from flask import Blueprint, request, make_response, jsonify
from sqlalchemy import or_, and_
from apps import db

# 创建一个蓝图，蓝图名称 permission，前缀 /permission
user_dp = Blueprint("permission", __name__, url_prefix="/permission")

# 后面写API接口 =============================================================
