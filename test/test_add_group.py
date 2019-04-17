# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

#это значок инициализатора фикстуры
@pytest.fixture
def app(request):
    #инициализация создания фикстуры
    fixture = Application()
    #указание как фикстура д.б. разрушена
    request.addfinalizer(fixture.destroy)
    return fixture

#тестовый метод принимающий в качестве параметра фикстуру и вызывающий в ней вспомогательные методы
#указываем, в каком пакете теперь искать про ЛОГИН и ЛОГАУТ
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="1234", header="qwert", footer="zxcvb"))
    app.session.logout()

    # it's rename double + noname + no header... = new test?
def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="", header="", footer=""))
    app.session.logout()