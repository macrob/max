from abc import ABC, abstractmethod
from enum import Enum, auto
from dataclasses import dataclass, field
from random import randint

class General(Enum):
    HEALTH = 100
    
#     NOT USED
# class d(Enum):
#   m = auto()
#   m2 = auto()
#   m3 = auto()
#   m4 = auto()  
# print(d.m2.value)

@dataclass(frozen=True)
class Params:
  DWARF_POWER = 24
  DWARF_ACCURACY = 20
  ELVES_POWER = 20
  ELVES_ACCURANCY = 90
  
class Charater(ABC):
  
  def __init__(self, name: str, power: int, accuracy: int) -> None:
    self.name = name
    self.health = General.HEALTH.value


    self.power = power
    self.accuracy = 10

  # def attack(self, other: Self):
  # @abstractmethod
  def attack(self, other: 'Charater'):
    print('-' * 20)

    if not self.is_alive:
      print(f'{self} is die')
      return False
    
    our_try = randint(1, 101)
    if our_try <= self.accuracy:
      other.health -= self.power
      print(f'{self} attacked {other}, health {other.health}')
      
      win_method = getattr(self, 'dance', None)
      if win_method:
        win_method()

      if not other.is_alive:
        print(f'{other} is die')
        return True
      else:
        print(f'{self.name} is missing attack')
        return False
        
        
    else:
      print(f'{self.name} missed')
      
  # def dance(self):
  #   raise NotImplementedError('dance is not implemented')
      
  
  @property
  def is_alive(self) -> bool:
    return self.health > 0


  @abstractmethod
  def __str__(self) -> str:
    return f'My name is {self.name} - {self.health}'
  
  def __repr__(self) -> str:
    return f'{type(self)} {self.name}'
    
    
  
  
class Dwarf(Charater):
  def __init__(self, name: str) -> None:
    power = Params.DWARF_POWER
    accuracy = Params.DWARF_ACCURACY

    super().__init__(name, power, accuracy)
  pass

  
  def __str__(self) -> str:
    return f'I am dwarf. My name is {self.name} - {self.health}'
  
  def dance(self):
    print(f'i am dancing')



class Elves(Charater):

  def __init__(self, name: str) -> None:
    power = Params.ELVES_POWER
    accuracy = Params.ELVES_ACCURANCY

    super().__init__(name, power, accuracy)

  def __str__(self) -> str:
    return f'I am Elves. My name is {self.name} - {self.health}'

d = Dwarf("Max")
e = Elves("Elf")

print(d)
print(e)


d_type = type(d)
d_is_dwarf = isinstance(d, Dwarf)
d_is_charater = isinstance(d, Charater)

d.attack(e)
d.attack(e)
d.attack(e)
d.attack(e)
d.attack(e)
d.attack(e)
d.attack(e)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)

ch = [Dwarf(str(randint(1, 10**9))) for _ in range(100)]
ch2 = [Elves(str(randint(1, 10**9))) for _ in range(100)]

# print(ch)
# print(ch2)
# print(ch[0])
# print(ch2[0])

pass