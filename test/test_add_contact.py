# -*- coding: utf-8 -*-
from model.contact import Contact
#from sys import maxsize

def test_add_contact(app):
    #unit4_09
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="Smit", firstname="Tom", home="000-00-00", mobile="222-22-22", work="3333333", phone2="111-11-11")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    #assert len(old_contacts) + 1 == len(new_contacts)
    #unit4_09
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

