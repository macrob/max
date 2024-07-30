from abc import ABC, abstractmethod
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
    def __init__(
        self, title: str, author_or_director: str, year: int, number_of_pages: int
    ) -> None:
        self.number_of_pages = number_of_pages
        super().__init__(title, author_or_director, year)

    def description(self):
        return f'{super().description()} Pages: {self.number_of_pages}'


class Magazine(LibraryItem):
    def __init__(
        self, title: str, author_or_director: str, year: int, issue_number: int
    ) -> None:
        self.issue_number = issue_number
        super().__init__(title, author_or_director, year)

    def description(self):
        return f'{super().description()} Issue Number: {self.issue_number}'


class DVD(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, duration: int) -> None:
        self.duration = duration
        super().__init__(title, author_or_director, year)

    def description(self):
        return f'{super().description()} Duration: {self.duration}'

book1 = Book('The Hobbit', 'J.R.R. Tolkien', 1937, 3)
book2 = Book('The Lord of the Rings', 'J.R.R. Tolkien', 1954, 12)
book3 = Book('The Silmarillion', 'J.R.R. Tolkien', 1977, 4)

magazine1 = Magazine('Time', 'Time Inc.', 1926, 1001)
magazine2 = Magazine('Time', 'Time Inc.', 1926, 1005)
magazine3 = Magazine('Time', 'Time Inc.', 1926, 1007)

dvd1 = DVD(
    'The Lord of the Rings: The Fellowship of the Ring', 'Peter Jackson', 2001, 178
)
dvd2 = DVD('The Lord of the Rings: The Two Towers', 'Peter Jackson', 2002, 179)
dvd3 = DVD(
    'The Lord of the Rings: The Return of the King', 'Peter Jackson', 2003, 201
)


def main():
  print(book1.description())
  print(book2.description())
  print(book3.description())

  print(magazine1.description())
  print(magazine2.description())
  print(magazine3.description())

  print(dvd1.description())
  print(dvd2.description())
  print(dvd3.description())

if (__name__ == '__main__'): 
  main()
