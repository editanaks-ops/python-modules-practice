# Функции форматирования для отчётов.

def format_book_data(data: dict) -> str:
    """
    Форматирует данные книги для отчёта.

    Пример:
    Title: 1984, Author: George Orwell, Genre: Dystopia
    """
    title = data.get("title", "Unknown title")
    author = data.get("author", "Unknown author")
    genre = data.get("genre", "Unknown genre")

    return f"Title: {title}, Author: {author}, Genre: {genre}"
