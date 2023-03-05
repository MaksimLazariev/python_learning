from timeit import timeit

from memory_profiler import profile

"""
Задача 22.
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются
в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого
множества. m - кол-во элементов второго множества. Затем пользователь вводит
сами элементы множеств.

1. Вводим списки
2. Найти пересечение (множество)
3. Упорядочить
"""


@profile
# метод ввода множества чисел через строку
def input_set(text):
    input_st = input(text).split()
    num_set = set(map(int, input_st))
    return num_set


# метод находит пересечение двух множеств и сортирует его по возрастанию
def sort_intersect(set01, set02):
    res_set = set01.intersection(set02)
    res_set = sorted(res_set)
    return res_set


# Вводим количество элементов в массивах, сами массивы, сразу делаем валидацию
try:
    number_of_elements_01 = int(input("Введите количество элементов в 1-м "
                                      "массиве: "))
    number_of_elements_02 = int(input("Введите количество элементов в 2-м "
                                      "массиве: "))

    numbers_set_01 = input_set("Введите 1-е множество чисел через пробел: ")
    numbers_set_02 = input_set("Введите 2-е множество чисел через пробел: ")

except ValueError:
    print("Введены неверные данные")
else:  # Проверяем, чтоб число элементов совпадало с размерами множеств
    if number_of_elements_01 == len(
            numbers_set_01) and number_of_elements_02 == len(numbers_set_02):
        # Находим отсортированное пересечение множеств и печатаем его
        result_set = sort_intersect(numbers_set_01, numbers_set_02)
        print("Итоговый список {}".format(result_set))
        # Замеряем время
        print("Время работы пересечения х 1000, {}".format(
            timeit("sort_intersect(numbers_set_01, numbers_set_02)",
                   number=1000, globals=globals())))
    else:
        print(
            "Количество введенных элементов не совпадает с размерами множеств")
