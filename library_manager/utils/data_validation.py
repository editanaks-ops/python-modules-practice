# Функции валидации данных книги.

def validate_book_data(data: dict) -> bool:
    """
    Проверяет корректность данных книги.

    Обязательные поля:
      - title (str, непустая)
      - author (str, непустая)
      - genre (str, непустая)
    """
    required_fields = ("title", "author", "genre")

    for field in required_fields:
        if field not in data:
            return False

        value = data[field]
        if not isinstance(value, str) or not value.strip():
            return False

    return True
