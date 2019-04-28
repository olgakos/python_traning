# -*- coding: utf-8 -*-
from model.contact import Contact

#задание 7-1
def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
#unit 3_05
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="timing contact"))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
