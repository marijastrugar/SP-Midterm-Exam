from enum import Enum


class Person:

    def __init__(self, name, surname, date_of_birth, address):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.address = address

    def __str__(self):
        return self.name + " " + self.surname


class Employee(Person):

    num_of_employees = 0

    def __init__(self, name, surname, date_of_birth, address, company, position, years_employed, base_salary):
        super(Employee, self).__init__(name, surname, date_of_birth, address)
        self.company = company
        self.position = position
        self.years_employed = years_employed
        self.base_salary = base_salary
        self.num_of_employees += 1

    def __str__(self):
        return super(Employee, self).__str__() + ", " + self.company + ", " + self.position

    def get_salary(self):