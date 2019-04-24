# -*- coding: utf-8 -*-
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
       wd = self.app.wd
       if text is not None:
         wd.find_element_by_name(field_name).click()
         wd.find_element_by_name(field_name).clear()
         wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        #стандартно переходим на нужную страницу "открыть стр. с группами"
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #submit deletion (выполнить клик по элементу кнопка) delete и кликнуть по нему"
        wd.find_element_by_name("delete").click()
        #затем обращение к методу "return_to_groups_page" чтобы перейти на стр групп
        self.return_to_groups_page()

    def select_first_group(self):
        # select first group (выполнить клик по элементу/чекбоксу)
        wd.find_element_by_name("selected[]").click()

    #это "вспомогательный метод" edit_first_group
    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit edition
        wd.find_element_by_name("edit").click()
        # fill group form (это блок кода, заполняющий ФОРМУ из трех полей name+header+footer)
        #-этот блок можно первратить во вспомю.метод для повторн. использования
        #-refactor-ectract-metod (+"group")=
        self.fill_group_form(group)
        # submit group edition/update
        #wd.find_element_by_name("update").click()
        wd.find_element_by_xpath("// input[@ name='update']").click()
        self.return_to_groups_page()

    def modify_first_group(self, new_group_date):
        #Открыть страницу с группами
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill group form
        self.fill_group_form(new_group_date)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("group page").click()

