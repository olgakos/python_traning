# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    #Unit3_05
    if app.group.count() == 0:
       app.group.create(Group(name="test3"))
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app):
    # Unit3_05
   if app.group.count() == 0:
      app.group.create(Group(name="test3"))
   app.group.modify_first_group(Group(header="New header"))