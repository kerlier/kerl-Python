#!/usr/bin/python3

class Employee:
    firstName = ''
    lastName = ''
    age = 0
    inCome = 0.0
    sex = 'M'
    def __init__(self):
        self.firstName = ''
        self.lastName = ''
        self.age = 0
        self.inCome = 0.0
        self.sex = 'M'
    def __init__(self, firstName, lastName, age, inCome, sex):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.inCome = inCome
        self.sex = sex
