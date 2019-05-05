# -*- coding: utf-8 -*-

from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


#unit3_06 Если выполняется условие что мы УЖЕ на стр.контакты, и кол-во записей "фамилия" >0, то делать переход на стр контакты не нужно
    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_link_text("Last name")) > 0):
           wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        # fill new contact
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.home)


    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        #внимание, не by_name а by_link
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
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
        wd.implicitly_wait(2)

    def edit_first_contact(self, contact):
        # две строки ниже можно скопировать из пхожих сценариев выше - "открыть стр. с группами"
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        #wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(contact)
        #????? self.fill_contact_form(new.)
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


#unit4_09+
    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(name=text, id=id))
        return contacts


