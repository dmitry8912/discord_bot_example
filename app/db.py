from typing import Any

from attr import dataclass


class Book:
    name: str
    description: str
    owner_name: str
    holder_name: str = None

class InMemoryBooksDatabase:
    __db = {}

    @classmethod
    def add_book(cls, key: str, value: Book):
        cls.__db[key] = value

    @classmethod
    def get_all_books(cls):
        for name, book in cls.__db.items():
            if book.holder_name is None:
                yield book

    @classmethod
    def read_book(cls, key: str, holder_name: str):
        book = cls.__db.get(key, None)
        if book:
            book.holder_name = holder_name

    @classmethod
    def return_book(cls, key: str):
        book = cls.__db.get(key, None)
        if book:
            book.holder_name = None

    @classmethod
    def my_books(cls, holder: str):
        for name, book in cls.__db.items():
            if book.holder_name == holder:
                yield book
