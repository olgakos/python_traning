# -*- coding: utf-8 -*-
#задание 7-1

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()