# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)


# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Company Name:', company_name, 'Location:', location)


# Child class
class Employee(Person, Company):
    def employee_info(self, name, age, company_name, location):
        print('Inside Employee class')
        self.person_info(name, age)
        self.company_info(company_name, location)

# creating object of child class
employee = Employee()

# calling the method of parent class using child class object
employee.employee_info('John', 25, 'Google', 'California')
employee.person_info('John', 25)
employee.company_info('Google', 'California')