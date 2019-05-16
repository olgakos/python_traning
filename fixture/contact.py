# -*- coding: utf-8 -*-
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


#-----------------------------------------------------
    # unit3_06 Если выполняется условие что мы УЖЕ на стр.контакты, и кол-во записей "фамилия" >0, то делать переход на стр контакты не нужно
    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_link_text("Last name")) > 0):
             wd.find_element_by_link_text("home").click()

# -----------------------------------------------------

    def fill_contact_form(self, contact):
        # fill new contact
        self.change_field_value("firstname", contact.firstname)
        #self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.home)

    def change_select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

#-----------------------------------------------------
    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation (внимание, не by_name а by_link)
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        #wd.find_element_by_xpath("//input[21]").click()
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

#15
    def add_contact_in_group(self, contact_id, group_name):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(contact_id)
        self.change_select_field_value("to_group", group_name)
        wd.find_element_by_name("add").click()
        self.return_group_page_with_contacts(group_name)
        self.contact_cache = None
#------------------------------------------------------
    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        ##wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # confirm changes
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

#Ранее было так:
    #def edit_first_contact(self, contact):
        # две строки ниже можно скопировать из пхожих сценариев выше - "открыть стр. с группами"
        #wd = self.app.wd
        #self.open_home_page()
        #wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        #self.fill_contact_form(contact)
        # confirm changes
        #wd.find_element_by_name("update").click()
        #self.return_to_home_page()
        #self.contact_cache = None

    def edit_first_contact(self, new_contact_data):
        #self.edit_contact_by_index(0)
        self.edit_contact_by_index(0, new_contact_data)
##

#15
    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # edit first contact
        self.select_contact_by_id(id)
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(new_contact_data)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None
#--------------------------------------------------------------

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # ожидание+ 2
        wd.implicitly_wait(2)
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        #ожидание+
        wd.find_element_by_css_selector("div.msgbox")
        # return to page contacts
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

#15
    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # return to page contacts
        wd.find_element_by_link_text("home").click()
        wd.implicitly_wait(2)
        self.contact_cache = None
#15
    def del_contact_in_group(self, contact_id, group_id, group_name):
        wd = self.app.wd
        self.open_group_page_with_contacts(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.return_group_page_with_contacts(group_name)
        self.contact_cache = None

#задание 7-1
    #def delete_first_contact(self):
        #wd = self.app.wd
        #self.open_home_page()
        #select first contact
        #wd.find_element_by_name("selected[]").click()
        #wd.find_element_by_xpath("//input[@value='Delete']").click()
        ##wd.find_element_by_name("delete").click()
        #wd.switch_to_alert().accept()
        # закрытие диалогового окна, в котором пользователь подтверждает удаление контакта
        #wd.find_element_by_link_text("home").click()
        #self.return_to_home_page()
        #wd.implicitly_wait(2)
        #self.contact_cache = None


    def delete_first_contact(self):
        self.delete_contact_by_index(0)


#----------------------------------------------------

#!!! 13
    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        #16if index == 1:
            #16wd.find_element_by_xpath("//td/input").click()
        #16else:
            #16wd.find_element_by_xpath("//tr[" + str(index+2) + "]/td/input").click()

#15
    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

#utit13
    #def select_first_contact(self):
        #wd = self.app.wd
        #wd.find_element_by_name("selected[]").click()

#--------------------------------------------------------

    def return_to_home_page(self):
        wd = self.app.wd
        # return contacts pages
        wd.find_element_by_link_text("home").click()

    # 14!!
    # def return_to_list_contacts_page(self):
    # wd = self.app.wd
    # wd.find_element_by_link_text("home page").click()

#лекц3_05
    def count(self):
        wd = self.app.wd
        self.open_home_page()
        #найти все элементы с selected , взять длину получ.списка и вернуть ее.
        #-это кол-ко контактов, которые присутст. в адерсной книге
        return len(wd.find_elements_by_name("selected[]"))

#Unit 4_10
    contact_cache = None

#unit4_09+
    def get_contact_list(self):
        if self.contact_cache is None:
          wd = self.app.wd
          self.open_home_page()
          self.contact_cache = []
          for element in wd.find_elements_by_name("entry"):
              text = element.text
              first_name = element.find_elements_by_xpath("td")[2].text
              last_name = element.find_elements_by_xpath("td")[1].text
              #first_name = element.find_element_by_name("selected[]").get_attribute("title"[0])
              #last_name = element.find_element_by_name("selected[]").get_attribute("title"[1])
              id = element.find_element_by_name("selected[]").get_attribute("value")
              self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id))
        return list(self.contact_cache)