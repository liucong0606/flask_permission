from apps import db

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
