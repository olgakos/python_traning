# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    #unit4_09
    old_contacts = app.contact.get_contact_list()
    #лекц 3_05-
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Timename2"))
    app.contact.edit_first_contact(Contact(firstname="Jhon", lastname="Svenson", home="222-22-22"))
    # unit4_09
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)