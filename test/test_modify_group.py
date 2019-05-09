# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    #unit4_09
    old_groups = app.group.get_group_list()
    group = Group(name="New group name")
    # Unit3_05
    if app.group.count() == 0:
         app.group.create(Group(name="test3"))
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    # unit 4_09
    new_groups = app.group.get_group_list()
    old_groups[0] = group


def test_modify_group_header(app):
   #un09
   old_groups = app.group.get_group_list()
   group = Group(header="New header")
   group.id = old_groups[0].id
   # Unit3_05
   if app.group.count() == 0:
       app.group.create(Group(name="test3"))
   app.group.modify_first_group(group)
   assert len(old_groups) == app.group.count()
   # unit 4_09
   new_groups = app.group.get_group_list()
