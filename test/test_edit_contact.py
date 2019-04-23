

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="Jhon", second_name="Svenson", home_phone="222-22-22"))
    #app.contact.edit_first_contact(Contact(firstname="new firstname"))
    app.session.logout()
