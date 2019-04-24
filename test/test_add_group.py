# -*- coding: utf-8 -*-
from model.group import Group

#тестовый метод принимающий в качестве параметра фикстуру и вызывающий в ней вспомогательные методы.
# В настоящее время fixture перенесенf в файл Conftest

#указываем, в каком пакете теперь искать про ЛОГИН и ЛОГАУТ
def test_add_group(app):
    #теперь метод ЛОГИН лежит в conftest как фикстура
    #app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="1234", header="qwert", footer="zxcvb"))
    #app.session.logout()

    # it's rename double + noname + no header... = new test?
def test_add_empty_group(app):
    #теперь метод ЛОГИН лежит в conftest как фикстура
    #app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="", header="", footer=""))
    #app.session.logout()