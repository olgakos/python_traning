# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group name")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#unit4_11
#def test_modify_group_name(app):
    #unit4_09
    #old_groups = app.group.get_group_list()
    #group = Group(name="New group name")
    # Unit3_05
    #if app.group.count() == 0:
         #app.group.create(Group(name="test3"))
    #app.group.modify_first_group(group)
    #assert len(old_groups) == app.group.count()
    # unit 4_09
    #new_groups = app.group.get_group_list()
    #old_groups[0] = group


def test_modify_group_name(app):
    if app.group.count() == 0:
          app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="New group name")
    group.id = old_groups[0].id
    #теперь надо писать modify_some_group?
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_header(app):
    # Unit3_05
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(header="New header name")
    group.id = old_groups[0].id
    # теперь надо писать modify_some_group?
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    # unit 4_09
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
