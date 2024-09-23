# Single inheritance is a way to inherit the properties of a class to another class.
# In single inheritance, a class is allowed to inherit from only one class.


# base/parent class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Parent(Vehicle) class')

# Child class 
class Car(Vehicle):
    def Car_info(self):
        print('Inside Child(Car) class')

# creating object of child class
car = Car()

# calling the method of parent class using child class object
car.Vehicle_info()
car.Car_info()