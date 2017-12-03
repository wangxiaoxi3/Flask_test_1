# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 下午9:17
# @Author  : WangJuan
# @File    : Model.py

from DB import db

class Environments(db.Model):
    __tablename__ = 'environments'
    #primary_key，设置为true，这列就是表对主键
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    create_time = db.Column(db.DateTime, nullable=True)
    def __init__(self, name):
        self.name = name

class Variable(db.Model):
    __tablename__ = 'variable1'
    #primary_key，设置为true，这列就是表对主键
    id = db.Column(db.Integer, primary_key=True)
    #nullable，如果设为 True ,这列允许使用空值;如果设为False ,这列不允许使用空值
    env_id = db.Column(db.Integer,db.ForeignKey('environments.id'), nullable=False)
    key = db.Column(db.String(1024), nullable=False)
    value = db.Column(db.String(1024), nullable=False)
    #nullable，如果设为 True ,这列允许使用空值;如果设为True ,这列允许使用空值
    create_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, env_id, key, value):
        self.env_id = env_id
        self.key = key
        self.value = value

