import datetime
from typing import Self
 
class Person:
  INITIAL_BALANCE = 50_000
  population = []
  
  @staticmethod
  def get_planet_position():
    return 'Earth is the third planet from the Sun and the only object in the Universe known to harbor life.'
  
  @classmethod
  def write_person_life(cls, person: Self, action: str):
    with open('life.csv', mode='a', encoding='utf-8') as life_file:
      for person in cls.population:
        life_file.write(f'{id(person)}, {person.name}, {action}, {cls.INITIAL_BALANCE}, {len(cls.population)}\n')
    pass
  def __init__(self, name: str, weight: float, birthday: datetime.datetime = None):
    self.name = name.title()
    self.birthday = birthday or datetime.datetime.now()

    self.__weight = weight    
    self.__money = self.INITIAL_BALANCE
    self.population.append(self)
    self.write_person_life(self, 'create')

  def run(self):
    print(f'I am running {self.name}')
    
  @property
  def person_weight(self) -> float:
    return self.__weight

  @person_weight.setter
  def person_weight(self, value: float):
    self.__weight = value
  
  @property
  def age(self) -> int:
    now = datetime.datetime.now()
    return (now - self.birthday).days // 365

  @property
  def money(self) -> float:
    return self.__money

  def __str__(self): 
    return f'{self.name} is {self.age} years old'
  
  def __repr__(self):
    return f'Person(name={self.name}, weight={self.weight}, birthday={self.birthday})'
  
  __repr__ == __str__
  
  def __del__(self):
    print(f'{self.name} is being deleted')
    # self.
    # self.population.remove(self)

  def transfer_money_to_another_person(self, other: Self, sum: float):
    if self.__money > sum:
      other.__money += sum
      self.__money -= sum

      print(f'{self.name} transferred {sum} to {other.name}')
    else:
      print(f'{self.name} has no money to transfer')
  
  def __eq__(self, other: Self) -> bool:
    return self.name == other.name and self.birthday == other.birthday
  


person1 = Person(name='John', weight=100, birthday=datetime.datetime(1990, 1, 1))
person2 = Person(name='Max', weight=4.200)
person3 = Person(name='Anton', weight=4.200)



person2.hobbies = ['programming', 'cooking']
person2.name = 'Alex'
person2._weight = 433443

print(f'{person2.person_weight=}')
person2.person_weight = 555
print(f'{person2.person_weight=}')

age = person1.age

person1.transfer_money_to_another_person(person2, 500000)
# print(person2.__dict__)

del person2

print(person1.INITIAL_BALANCE)
Person.INITIAL_BALANCE = 1000
print(person1.INITIAL_BALANCE)

del person1
del Person.population[0]

print(Person.get_planet_position())
print()


# print(person1)

