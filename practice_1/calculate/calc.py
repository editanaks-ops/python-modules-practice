# practice_1/calculate/calc.py

def evaluate(x, y, power: int):
    """
    Пример функции для демонстрации импортов.

    1. Преобразуем x и y к float
    2. Складываем
    3. Возводим сумму в степень power

    Пример:
    x = "5", y = 5, power = 2 -> (5 + 5) ** 2 = 100.0
    """
    x = float(x)
    y = float(y)
    return (x + y) ** power
