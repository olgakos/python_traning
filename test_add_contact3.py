# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact3(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact3(self):
        wd = self.wd
        #open home page
        wd.get("http://localhost/addressbook/addressbook/")
        #login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        #password
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        #enter
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_id("content").click()
        #init new contact
        wd.find_element_by_link_text("add new").click()
        #fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Tom")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Smit")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("111-11-11")
        #submit contact creation
        wd.find_element_by_xpath("//input[21]").click()
        #return contacts pages
        wd.find_element_by_id("content").click()
        #logout
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
