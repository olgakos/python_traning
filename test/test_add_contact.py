# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

#это значок инициализатора фикстуры
@pytest.fixture
def app(request):
    #инициализация создания фикстуры
    fixture = Application()
    #указание как фикстура д.б. разрушена
    request.addfinalizer(fixture.destroy)
    return fixture

#тестовый метод принимающий в качестве параметра фикстуру и вызывающий в ней вспомогательные методы
#указываем, в каком пакете теперь искать про записанные данные констакта.
#если сломается - попробуй TestAddContact / test_add_contact
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact(first_name="Tom", second_name="Smit", home_phone="111-11-11"))
    app.session.logout()