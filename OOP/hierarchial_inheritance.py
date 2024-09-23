class Vehivle:
    def info(self):
        print('This is Vehicle')


class Car(Vehivle):
    def car_info(self, name):
        print('Car name is:', name)


class Truck(Vehivle):
    def truck_info(self, name):
        print("Truck name is :", name)


obj1 = Car()
obj1.info()
obj1.car_info('Bmw')

obj2 = Truck()
obj2.info()
obj2.truck_info('Isuzu')