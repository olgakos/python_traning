# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_edit_some_contact(app):
    if app.contact.count() == 0:
          app.contact.create(Contact(firstname="Timename2"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Jhon", lastname="Svenson", home="222-22-22")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    #def test_edit_first_contact_dates(app):
        #if app.contact.count() == 0:
            #app.contact.create(Contact(firstname="Sam"))
        #old_contacts = app.contact.get_contact_list()
        #contact = Contact(bday="23", bmonth="April", byear="2000",
                          #aday="03", amonth="October", ayear="1928")
        #contact.id = old_contacts[0].id
        #app.contact.edit_first_contact(contact)
        #assert len(old_contacts) == app.contact.count()
        #new_contacts = app.contact.get_contact_list()
        #old_contacts[0] = contact
        # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_first_contact(app):
    # Unit3_05
    if app.contact.count() == 0:
          app.contact.create(Contact(firstname="Timename3"))
    #unit4_09
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Jhon", lastname="Svenson", home="222-22-22")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


