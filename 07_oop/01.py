class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + ' !'
    
    def set_brand(self, brand):
        self.__brand = brand

    def fullname(self):
        return f'{self.__brand} {self.__model}'
    
    def fuel_type(self):
        return 'Petrol or Diesel'

    @property
    def model(self):
        return self.__model
    
    @staticmethod
    def general_description():
        return 'Cars are amazing'
  
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return 'Electric charge'


'''
# car = Car('Toyota', 'Corolla')

# print(car.brand)
# print(car.model)
# print(car.fullname())

# car2 = Car('Tesla', 'Model S')

# print(car2.brand)
# print(car2.model)
# print(car2.fullname())

car3 = Electric_Car('Tesla', 'Model Y', '85kWh')

# print(car3.__brand)
# print(car3.get_brand())
# print(car3.model)
# car3.set_brand('Audi')
# car3.model = 'Electron'
# print(car3.get_brand())
# print(car3.model)
# print(car3.fuel_type())
# print(car3.fullname())
# print(car3.battery_size)

# print(isinstance(car3, Electric_Car))
# print(issubclass(Electric_Car, Car))

safari = Car('Tata', 'Safari')
safari3 = Car('Tata', 'Nexon3')

# print(safari.general_description())
# print(Car.general_description())

# print(Car.total_car)

# safari.model = 'City'  # Not allowed because model is private
# print(safari.model)
'''

# my_tesla = Electric_Car('Tesla', 'Model S', '85kWh')
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, Electric_Car))

class Battery:
    def battery_info(self):
        return 'This is battery'

class Engine:
    def engine_info(self):
        return 'This is engine'

class Electic_Car_Two(Car, Battery, Engine):
    pass

my_new_tesla = Electic_Car_Two('Tesla', 'Model S')

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())

print(isinstance(my_new_tesla, Battery))
print(isinstance(my_new_tesla, Engine))
