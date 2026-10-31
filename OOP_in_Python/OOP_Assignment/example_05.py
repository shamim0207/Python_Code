from abc import ABC
class vehicle(ABC):
    brand="BMW"
    model="X-series_SUVs"
    def get_view():
        pass

class car(vehicle):
    def get_view(self,seats):
        print(f"car brand name is {self.brand} , car model is {self.model} and seats in car: {seats}")


class bike(vehicle):
    def get_view(self,engine_cc):
        print(f"Bike brand name is {self.brand} , bike model is {self.model} and engine_CC: {engine_cc}")


#========================================================================

car=car()
car.get_view(50)


bike=bike()
bike.get_view(165)