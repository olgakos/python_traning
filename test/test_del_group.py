# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    #unit4_09
    old_groups = app.group.get_group_list()
    #лекц 3_05-
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
    # unit4_09 "внимание, минус группа, а не + группа как в test_add_group"
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

