from typing import Self

# // витрата палива

class Car:
  def __init__(self, *, manufacturer: str, model: str, fuel_efficiency: float, year: int = 2020):
    self.__manufacturer = manufacturer
    self.__model = model
    self.__year = year

    self.__fuel_efficiency = fuel_efficiency # l/100km
    
    self.__mileage = 0
    
  @property
  def mileage(self) -> int:
    return self.__mileage
  
  @mileage.setter
  def mileage(self, value: int) -> None:
    self.__mileage = value

  def __str__(self): 
    if self.__fuel_efficiency:
      return f'Car {self.__manufacturer} {self.__model} {self.__year} with fuel efficiency {self.__fuel_efficiency} l/100km'
    else :
      return f'Car {self.__manufacturer} {self.__model} {self.__year} this is electric car'
    
    
    
car1 = Car('BMW', 'M5', 20)
cae3 = Car(manufacturer='Tesla', model='Model S', fuel_efficiency=0, year=2021)
car2 = Car('Tesla', 'Model S', 0)

print(car1)
print(car2)