from abs import ABC, abstractmethod
from enum import Enum, auto
from dataclasses import dataclass, field
from random import randint

class LibraryItem(ABC):
  def __init__(self, title: str, author_or_director: str, year: int) -> None:
    self.title = title
    self.author_or_director = author_or_director
    self.year = year
    
  @abstractmethod
  def description(self):
    return f'Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year})'
    
class Book(LibraryItem):
  def __init__(self, title: str, author_or_director: str, year: int, number_of_pages: int) -> None:
    self.number_of_pages = number_of_pages
    super().__init__(title, author_or_director, year)
  
  def description(self):
    return f'{super().description()} Pages: {self.number_of_pages}'
  
class Magazine(LibraryItem):
  def __init__(self, title: str, author_or_director: str, year: int, issue_number: int) -> None:
    self.issue_number = issue_number
    super().__init__(title, author_or_director, year)
    
  def description():
    return f'{super().description()} Issue Number: {self.issue_number}'
  
class Dvd(LibraryItem):
  def __init__(self, title: str, author_or_director: str, year: int, duration: int) -> None:
    self.duration = duration
    super().__init__(title, author_or_director, year)

  def description(self):
    return f'{super().description()} Duration: {self.duration}'