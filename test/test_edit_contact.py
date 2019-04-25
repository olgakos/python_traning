# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    #лекц 3_05-
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Timename2"))
    app.contact.edit_first_contact(Contact(first_name="Jhon", second_name="Svenson", home_phone="222-22-22"))