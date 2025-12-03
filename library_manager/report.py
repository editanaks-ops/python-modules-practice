# Генерация отчётов по библиотеке.

from .catalog import Library
from .utils import format_book_data


def generate_report(library: Library) -> str:
    """
    Генерирует текстовый отчёт по всем книгам в библиотеке.

    Возвращает многострочную строку.
    """
    books = library.list_books()

    lines: list[str] = []
    lines.append("LIBRARY REPORT")
    lines.append("-" * 40)
    lines.append(f"Total books: {len(books)}")

    if not books:
        lines.append("Library is empty.")
        return "\n".join(lines)

    lines.append("")
    lines.append("Books:")
    for book in books:
        lines.append(f"- {format_book_data(book)}")

    return "\n".join(lines)
