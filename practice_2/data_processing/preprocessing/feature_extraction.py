# data_processing/preprocessing/feature_extraction.py

from typing import List, Dict


def compute_basic_stats(values: List[float]) -> Dict[str, float]:
    """
    Вычисляет простые статистики: min, max, mean.
    Если список пустой — поднимает ValueError.
    """
    if not values:
        raise ValueError("Нельзя посчитать статистики по пустому списку")

    minimum = min(values)
    maximum = max(values)
    mean = sum(values) / len(values)

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
    }

