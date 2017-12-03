#!/usr/bin/python
#-*- coding: UTF-8 -*-

from __future__ import unicode_literals

from flask import (Flask, render_template, redirect, url_for, request, flash)
from flask_bootstrap import Bootstrap
from Model import Variable, Environments
from Forms import VariableListForm,EnvironmentsListForm
from DB import db

SECRET_KEY = 'This is my key wj'

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = SECRET_KEY

#制定mysql的地址：mysql://username:password@hostname/database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:wangjuan@localhost:3306/flask?charset=utf8mb4"
#如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def show_environments_list():
    form = EnvironmentsListForm()
    if request.method == 'GET':
        #query.all()返回查询到的所有对象
        envlists = Environments.query.all()
        return render_template('index.html', envlists=envlists, form=form)
    else:
        if form.validate_on_submit():
            entlist = Environments(form.name.data)
            #add()插入数据
            db.session.add(entlist)
            #commit()提交事务
            db.session.commit()
            flash('You have add a new environments')
        else:
            flash(form.errors)
        return redirect(url_for('show_environments_list'))


@app.route('/delete/<int:id>')
def delete_environments_list(id):
    #first_or_404() 返回查询的第一个结果，如果没有结果，则终止请求，返回 404 错误响应
    envlist1 = Environments.query.filter_by(id=id).first_or_404()
    # delete()删除数据
    db.session.delete(envlist1)
    db.session.commit()
    flash('You have delete a Environments')
    return redirect(url_for('show_environments_list'))



@app.route('/view/<int:env_id>', methods=['GET', 'POST'])
def show_variable_list(env_id):
    form = VariableListForm()
    if request.method == 'GET':
        #filter_by() 把等值过滤器添加到原查询上，返回一个新查询
        variablelists = Variable.query.filter_by(env_id=env_id).join(Environments, Variable.env_id == Environments.id)
        return render_template('view.html', variablelists=variablelists, form=form)
    else:
        if form.validate_on_submit():
            variablelist = Variable(form.env_id.data,form.key.data, form.value.data)
            #add()插入数据
            db.session.add(variablelist)
            #commit()提交事务
            db.session.commit()
            flash('You have add a new Variable')
        else:
            flash(form.errors)
        return redirect(url_for('show_variable_list',_external=True,env_id=env_id))


@app.route('/change/<int:env_id>/<int:id>', methods=['GET', 'POST'])
def change_variable_list(env_id,id):
    if request.method == 'GET':
        variablelists = Variable.query.filter_by(env_id=env_id,id=id).join(Environments,Variable.env_id == Environments.id).first_or_404()
        form = VariableListForm()
        form.env_id.data = variablelists.env_id
        form.key.data = variablelists.key
        form.value.data = variablelists.value
        return render_template('modify.html', form=form)
    else:
        form = VariableListForm()
        if form.validate_on_submit():
            variablelists = Variable.query.filter_by(env_id=env_id,id=id).join(Environments,Variable.env_id == Environments.id).first_or_404()
            variablelists.env_id = form.env_id.data
            variablelists.key = form.key.data
            variablelists.value = form.value.data
            db.session.add(variablelists)
            db.session.commit()
            flash('You have modify a variablelist')
        else:
            flash(form.errors)
        return redirect(url_for('show_variable_list',_external=True,env_id=env_id))

@app.route('/delete/<int:env_id>/<int:id>')
def delete_variable_list(env_id,id):
    #first_or_404() 返回查询的第一个结果，如果没有结果，则终止请求，返回 404 错误响应
    variablelists = Variable.query.filter_by(env_id=env_id, id=id).join(Environments,Variable.env_id == Environments.id).first_or_404()
    # delete()删除数据
    db.session.delete(variablelists)
    db.session.commit()
    flash('You have delete a variable')
    return redirect(url_for('show_variable_list',_external=True,env_id=env_id))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
