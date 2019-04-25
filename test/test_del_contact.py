# -*- coding: utf-8 -*-
from model.contact import Contact

#задание 7-1
def test_delete_first_contact(app):
#unit 3_05
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="timing contact"))
    app.contact.delete_first_contact()
