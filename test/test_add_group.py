# -*- coding: utf-8 -*-
from model.group import Group
#from sys import maxsize

def test_add_group(app):
    #unit 4_09
    #очевидно, список групп old_groups прочитан с неправильной страницы. вероятно, тест не пытается открывать в начале нужную страницу, так что остается открыта та, которая была открыта в конце предыдущего теста
    old_groups = app.group.get_group_list()
    group = Group(name="name of Group", header="header of Group", footer="Footer of Group")
    app.group.create(group)
    #unit4_09
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
#вставка к4_11
    #def id_or_max(gr):
        #if gr.id:
            #return gr.id
        #else:
            #return maxsize
#unit4_11 (10-30)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
