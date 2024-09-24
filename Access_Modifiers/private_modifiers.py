class Student:
    __schoolName = 'XYZ School'

    def __init__(self, name, age):
        self.__name = name
        self.__salary = age
    def __display(self):
        print('This is a private method')