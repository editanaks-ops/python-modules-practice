# data_processing/preprocessing/data_cleaning.py
from typing import List, Any


def remove_none(values: List[Any]) -> List[Any]:
    """Удаляет все значения None из списка."""
    return [v for v in values if v is not None]


def remove_negatives(values: List[float]) -> List[float]:
    """Удаляет отрицательные числа из списка."""
    return [v for v in values if v >= 0]

