# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')


# Create object of sportsCar
s_car = SportsCar()

# Access Vehicles's and car info
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()
