"""
Задача 26:
Напишите программу, которая на вход принимает два числа A и B, и возводит
число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
"""

# Рекурсивная функция подсчета степени
def degree_count(num, deg):
    # Проверяем базовое значение
    if deg == 1:
        return num
    # делаем произведение числа и рекурсии
    else:
        return num * degree_count(num, deg - 1)


try:  # Делаем валидацию ввода чисел
    number = int(input("Введите число: "))
    degree = int(input("Введите степень: "))
except ValueError:
    print("вы ввели не число")
# Если все хорошо, запускаем подсчет степени
else:
    result = degree_count(number, degree)
    print("Число {} в степени {} равно {}".format(number, degree, result))
