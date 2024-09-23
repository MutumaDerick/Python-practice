class Vehicle:
    def Vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

s_car = SportsCar()
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()