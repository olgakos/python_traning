# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    #app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Name_afret_edit", header="Header_after_edit", footer="Footer_after_edit"))
    #app.group.edit_first_group(Group("Name_afret_edit","Header_after_edit","Footer_after_edit"))
    #app.session.logout()