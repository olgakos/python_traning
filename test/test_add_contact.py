# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    #unit4_09
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="Tom", second_name="Smit", home_phone="111-11-11"))
    #unit4_09
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
