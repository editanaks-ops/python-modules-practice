# Управление библиотекой книг.

from typing import List, Dict
from .utils import validate_book_data


class Library:
    """
    Класс для управления библиотекой.

    Книги хранятся как словари:
    {
        "title": str,
        "author": str,
        "genre": str,
    }
    """

    def __init__(self) -> None:
        self._books: List[Dict[str, str]] = []

    def add_book(self, title: str, author: str, genre: str) -> bool:
        """
        Добавляет книгу в библиотеку.

        Возвращает True, если данные корректны и книга добавлена,
        иначе False (книга не добавляется).
        """
        data = {"title": title, "author": author, "genre": genre}

        if not validate_book_data(data):
            return False

        self._books.append(data)
        return True

    def remove_book(self, title: str) -> bool:
        """
        Удаляет первую найденную книгу по названию.

        Возвращает True, если книга была найдена и удалена,
        иначе False.
        """
        for index, book in enumerate(self._books):
            if book.get("title") == title:
                del self._books[index]
                return True
        return False

    def find_by_title(self, title: str) -> List[Dict[str, str]]:
        """Возвращает список книг с заданным названием."""
        return [book for book in self._books if book.get("title") == title]

    def find_by_author(self, author: str) -> List[Dict[str, str]]:
        """Возвращает список книг указанного автора."""
        return [book for book in self._books if book.get("author") == author]

    def find_by_genre(self, genre: str) -> List[Dict[str, str]]:
        """Возвращает список книг указанного жанра."""
        return [book for book in self._books if book.get("genre") == genre]

    def list_books(self) -> List[Dict[str, str]]:
        """Возвращает копию списка всех книг."""
        return self._books.copy()
