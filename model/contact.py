# -*- coding: utf-8 -*-
from sys import maxsize

#это класс Contact из задания №3
class Contact():

  def __init__(self, firstname="None", lastname="None", home="None", id="None", name="None"):
        self.firstname = firstname
        self.lastname = lastname
        self.home = home
        self.id = id
        self.name = name



  def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)


  def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname


  def id_or_max(self):
        if self.id:
              return int(self.id)
        else:
              return maxsize