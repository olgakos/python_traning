# -*- coding: utf-8 -*-
from sys import maxsize

#это класс Contact из задания №3
class Contact():

  def __init__(self, firstname=None, lastname=None, id=None,
               address=None, email=None, email2=None,
               homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
               all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.email2 = email2
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page=all_phones_from_home_page
        self.id = id



  def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)


  def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

# unit 4_11 (10-05)
  def id_or_max(self):
      if self.id:
          return int(self.id)
      else:
          return maxsize