class Student:
    schoolName = 'PLP Academy'

    def __init__(self, name , age):
        self.name = name
        self.age = age

# How to access public members
std = Student("Mkuu", 25)
print(std.schoolName)  # 'PLP Academy'
print(std.name)        # 'Mkuu'
std.age = 28
print(std.age)         # 28