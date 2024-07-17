import datetime
from typing import Self
 
class Person:
  def __init__(self, name: str, weight: float, birthday: datetime.datetime = None):
    self.name = name.title()
    self.birthday = birthday or datetime.datetime.now()

    self.__weight = weight    
    self.__money = 50_000

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

  def __str__(self): 
    return f'{self.name} is {self.age} years old'
  
  def __repr__(self):
    return f'Person(name={self.name}, weight={self.weight}, birthday={self.birthday})'
  
  __repr__ == __str__
  
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
person2 = Person(name='Jane', weight=4.200)



person2.hobbies = ['programming', 'cooking']
person2.name = 'Alex'
person2._weight = 433443

print(person2.person_weight)
person2.person_weight = 555

print(person2.person_weight)

age = person1.age

person1.transfer_money_to_another_person(person2, 500000)
print(person2.__dict__)
print(person1)