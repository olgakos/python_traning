# -*- coding: utf-8 -*-
from model.group import Group

#тестовый метод принимающий в качестве параметра фикстуру и вызывающий в ней вспомогательные методы.
# В настоящее время fixture перенесенf в файл Conftest

#указываем, в каком пакете теперь искать про ЛОГИН и ЛОГАУТ
def test_add_group(app):
    #теперь метод ЛОГИН лежит в conftest как фикстура
    #app.session.login(username="admin", password="secret")
    #unit 4_09
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="name of Group", header="header of Group", footer="Footer of Group"))
    #unit4_09
    new_groups = app.group.get_group_list()
    #"длина старого списка групп +1 равна длине нового списка груп"
    assert  len(old_groups) + 1 == len(new_groups)
    #app.session.logout()

    # it's rename double + noname + no header... = new test?
def test_add_empty_group(app):
    #теперь метод ЛОГИН лежит в conftest как фикстура
    #app.session.login(username="admin", password="secret")
    # unit 4_09
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="", header="", footer=""))
    #unit4_09
    new_groups = app.group.get_group_list()
    #"длина старого списка групп +1 равна длине нового списка груп"
    assert  len(old_groups) + 1 == len(new_groups)
    #app.session.logout()