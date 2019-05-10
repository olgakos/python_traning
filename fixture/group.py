# -*- coding: utf-8 -*-
from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        #unit3_06 Если выполняется условие что мы УЖЕ на стр.Гр. и кол-во кнопок new >0, то делать переход на стр Гр. не нужно
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
           wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        #unit 4_10
        self.group_cache = None


    def modify_first_group(self, new_group_date):
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
        # unit 4_10
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
       wd = self.app.wd
       if text is not None:
           wd.find_element_by_name(field_name).click()
           wd.find_element_by_name(field_name).clear()
           wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        # !!! след.строку удалить?? есть в лекц 3_05 (UPD строка нужна, иначе падает)
        wd = self.app.wd
        # select first group (выполнить клик по элементу/чекбоксу)
        wd.find_element_by_name("selected[]").click()

        # unit 4_11
    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

#unit4_11
    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        # unit 4_10
        self.group_cache = None


    #def delete_first_group(self):
        #wd = self.app.wd
        #self.open_groups_page()
        #self.select_first_group()
        ##submit deletion (выполнить клик по элементу кнопка) delete и кликнуть по нему"
        #wd.find_element_by_name("delete").click()
        ##затем обращение к методу "return_to_groups_page" чтобы перейти на стр групп
        #self.return_to_groups_page()
        ## unit 4_10
        #self.group_cache = None

    #это "вспомогательный метод" edit_first_group
    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # + u4_10
        self.select_first_group()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit edition
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit group edition/update
        #wd.find_element_by_name("update").click()
        wd.find_element_by_xpath("// input[@ name='update']").click()
        self.return_to_groups_page()
        #unit 4_10
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

#лекц3_05
    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        #найти все элеемнты с selected , взять длину получ.списка и вренуть ее.
        #-это кол-ко групп, которые присутст. в адерсной книге
        return len(wd.find_elements_by_name("selected[]"))

    #unit4_10
    group_cache = None

    #unit4_09 добавляем метод
    #unit4_10 cache
    def get_group_list(self):
        if self.group_cache is None:
           wd = self.app.wd
           self.open_groups_page()
           self.group_cache = []
           for element in wd.find_elements_by_css_selector("span.group"):
               text = element.text
               id = element.find_element_by_name("selected[]").get_attribute("value")
               self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)