# -*- coding: utf-8 -*-
# fixture перенесена в файл Conftest
#указываем, в каком пакете теперь искать про ЛОГИН и ЛОГАУТ
from model.group import Group

def test_modify_group_name(app):
    app.group.modyfy_first_group(Group(name="New group"))
    #app.session.logout()

def test_modify_group_header(app):
    #app.session.login(username="admin", password="secret")
    app.group.modyfy_first_group(Group(header="New header"))
    #app.session.logout()