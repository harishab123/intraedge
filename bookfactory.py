from abc import ABC, abstractmethod
from Book import Book

class BookFactory(ABC):
    @abstractmethod
    def create_book(self, title, author, isbn):
        pass

class ConcreteBookFactory(BookFactory):
    def create_book(self, title, author, isbn):
        return Book(title, author, isbn)
