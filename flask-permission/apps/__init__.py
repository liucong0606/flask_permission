from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# 获取 Flask 的 app对象
def get_app():
    app = Flask(__name__)
    # 应用自动刷新
    app.debug = True
    # 应用ip/端口 配置
    app.config['SERVER_NAME'] = '127.0.0.1:5000'
    # 数据库连接配置
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1/db_flask_stu?charset=utf8"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # 注册蓝图
    from apps.user import user_dp
    app.register_blueprint(user_dp)

    return app
