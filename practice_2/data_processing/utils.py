# data_processing/utils.py

from typing import Iterable


def ensure_iterable(obj) -> bool:
    """Проверяет, что объект итерируемый (но не строка)."""
    if isinstance(obj, (str, bytes)):
        return False
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def to_float_list(values: Iterable) -> list[float]:
    """
    Преобразует элементы в список float.
    Некорректные элементы вызывают ValueError.
    """
    result = []
    for v in values:
        try:
            result.append(float(v))
        except (TypeError, ValueError) as e:
            raise ValueError(f"Нельзя преобразовать {v!r} к float") from e
    return result

