# -*- coding: utf-8 -*-
from enum import Enum, unique

@unique
class a(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = a(gender.value)


