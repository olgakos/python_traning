# -*- coding: utf-8 -*-
#это отдельный класс application (app) где содержатся все вспом.методы
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        #self.wd = WebDriver()
        self.wd = webdriver.Firefox()
        #Unit3_06 строка ниже полезна больше для динамических страниц, время на догрузку
        #self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/addressbook/")


    def destroy (self):
        self.wd.quit()