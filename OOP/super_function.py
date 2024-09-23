# Python also has a super() function that will make the child class inherit all the methods and properties from its parent

class Company:
    def company_name(self):
        return 'Google'
    

class Employee(Company):
    def info(self):
        c_name = super().company_name()
        print("Jessica works at", c_name)

emp = Employee()
emp.info()