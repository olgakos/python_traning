# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


#это значок инициализатора фикстуры
@pytest.fixture
def app(request):
    #инициализация создания фикстуры
    fixture = Application()
    #указание как фикстура д.б. разрушена
    request.addfinalizer(fixture.destroy)
    return fixture

#тестовый метод принимающий в качестве параметра фикстуру и вызывающий в ней вспомогательные методы
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="1234", header="qwert", footer="zxcvb"))
    app.logout()

    # it's rename double + noname + no header... = new test?
def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()