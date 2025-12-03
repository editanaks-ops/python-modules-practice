# data_processing/core.py
from typing import Iterable, Dict, Any, List
from .utils import ensure_iterable, to_float_list
from .preprocessing import remove_none, remove_negatives, compute_basic_stats
from .postprocessing import generate_text_report, build_text_histogram


def process_data(raw_values: Iterable[Any]) -> Dict[str, Any]:
    """
    Полный цикл обработки данных:
    - проверка, что данные итерируемые
    - удаление None
    - преобразование к float
    - удаление отрицательных чисел
    - вычисление статистик
    - генерация отчета и "визуализации"
    """
    if not ensure_iterable(raw_values):
        raise TypeError("Ожидался итерируемый объект (например, список чисел)")

    # Преобразуем вход в список, чтобы можно было передавать его в функции несколько раз
    raw_list = list(raw_values)

    # 1) Удаляем None
    no_none: List[Any] = remove_none(raw_list)

    # 2) Преобразуем к float (здесь None уже нет)
    numeric_values: List[float] = to_float_list(no_none)

    # 3) Удаляем отрицательные значения
    cleaned: List[float] = remove_negatives(numeric_values)

    # 4) Считаем статистики
    stats = compute_basic_stats(cleaned)

    # 5) Строим отчет
    report = generate_text_report(cleaned, stats)

    # 6) "Визуализация"
    histogram = build_text_histogram(cleaned)

    return {
        "cleaned_values": cleaned,
        "stats": stats,
        "report": report,
        "histogram": histogram,
    }

