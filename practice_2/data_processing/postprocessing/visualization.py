# data_processing/postprocessing/visualization.py

from typing import List


def build_text_histogram(values: List[float]) -> str:
    """
    Строит простой текстовый "гистограммоподобный" график.
    Каждое значение — строка из * соответствующей длины.
    """
    lines = ["Текстовая визуализация (условная гистограмма):"]

    if not values:
        lines.append("Нет данных для отображения.")
        return "\n".join(lines)

    max_value = max(values) or 1  # защита от деления на 0

    for v in values:
        bar_length = int((v / max_value) * 40)  # максимум 40 символов
        bar = "*" * bar_length
        lines.append(f"{v:>6.2f}: {bar}")

    return "\n".join(lines)

