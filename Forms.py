# -*- coding: utf-8 -*-
# @Time    : 2017/11/30 下午2:53
# @Author  : WangJuan
# @File    : Forms.py

from __future__ import unicode_literals
from flask_wtf import Form

from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length

class VariableListForm(Form):
    env_id = StringField('env_id',validators=[DataRequired(),Length(1,64)])
    key = StringField('key', validators=[DataRequired(), Length(1, 64)])
    value = StringField('value', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')

class EnvironmentsListForm(Form):
    name = StringField('name', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')

