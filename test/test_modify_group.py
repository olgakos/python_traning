# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    #unit4_09
    old_groups = app.group.get_group_list()
    #Unit3_05
    if app.group.count() == 0:
       app.group.create(Group(name="test3"))
    app.group.modify_first_group(Group(name="New group"))
    #unit 4_09
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
   #unit4_09
   old_groups = app.group.get_group_list()
    # Unit3_05
   if app.group.count() == 0:
      app.group.create(Group(name="test3"))
   app.group.modify_first_group(Group(header="New header"))
   # unit 4_09
   new_groups = app.group.get_group_list()
   assert len(old_groups) == len(new_groups)