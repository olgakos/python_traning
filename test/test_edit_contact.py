# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    #unit4_09
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Jhon", lastname="Svenson", home="222-22-22")
    #Unit3_05
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Timename2"))
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
