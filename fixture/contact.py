
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self, wd):
        # enter
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_id("content").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        # !удалила из этого места строчку self.create_new_contact() вроде запустилось.
        # init new contact
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
        wd.find_element_by_xpath("//input[21]").click()

    def return_to_contacts_page(self):
        wd = self.app.wd
        # return contacts pages
        wd.find_element_by_id("content").click()
