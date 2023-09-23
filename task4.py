# Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.


from typing import List
from math import sqrt


def correlation_pearson(array_1: List[float], array_2: List[float]) -> float:
    """ Расчет корреляции Пирсона между двумя массивами. """

    if len(array_1) != len(array_2):
        raise ValueError("Длина массивов должна быть одинаковой")

    n = len(array_1)

    average_1 = sum(array_1) / n
    average_2 = sum(array_2) / n

    covariance = sum((array_1[i] - average_1) *
                     (array_2[i] - average_2) for i in range(n))
    variance_array_1 = sum((x - average_1) ** 2 for x in array_1)
    variance_array_2 = sum((y - average_2) ** 2 for y in array_2)

    correlation = covariance / \
        (sqrt(variance_array_1) * sqrt(variance_array_2))

    return round(correlation)


arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

correlation = correlation_pearson(arr_1, arr_2)
print(f"Расчёт корреляции Пирсона = {correlation}")
