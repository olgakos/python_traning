# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    #unit4_09
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Tom", lastname="Smit", home="111-11-11")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    #unit4_09
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

