# -*- coding: utf-8 -*-

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        #внимание, не by_name а by_link
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.second_name)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        # submit contact creation
        #wd.find_element_by_xpath("//input[21]").click()
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

#задание 7-1
    def delete_first_contact(self):
        # две строки ниже можно скопировать из пхожих сценариев выше - "открыть стр. с группами"
        wd = self.app.wd
        self.open_home_page()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.find_element_by_name("delete").click()
        wd.switch_to_alert().accept()
        # закрытие диалогового окна, в котором пользователь подтверждает удаление контакта
        #wd.find_element_by_link_text("home").click()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        # две строки ниже можно скопировать из пхожих сценариев выше - "открыть стр. с группами"
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        #wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.second_name)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        #self.fill_contact_form(contact)
        # confirm changes
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        # return contacts pages
        wd.find_element_by_link_text("home").click()

#лекц3_05
    def count(self):
        wd = self.app.wd
        self.open_home_page()
        #найти все элементы с selected , взять длину получ.списка и вернуть ее.
        #-это кол-ко контактов, которые присутст. в адерсной книге
        return len(wd.find_elements_by_name("selected[]"))
