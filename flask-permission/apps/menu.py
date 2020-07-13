from flask import Blueprint, request, make_response, jsonify
from sqlalchemy import or_, and_
from apps import db

# 创建一个蓝图，蓝图名称 menu，前缀 /menu
user_dp = Blueprint("menu", __name__, url_prefix="/menu")

# 后面写API接口 =============================================================
