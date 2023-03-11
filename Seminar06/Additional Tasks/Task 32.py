"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше
заданного максимума)

Решение:
1. Вводим данные (список и границы)
2. Находим индексы, заносим их в новый список
3. Выводим готовый список
"""

try:
    # input_string = input("Введите  список чисел через пробел: ").split()
    # input_list = list(map(int, input_string))
    input_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0,
                  -5, -5, 7]
    min_num = int(input("Введите  минимум: "))
    max_num = int(input("Введите максимум: "))
except ValueError:
    print("Ошибка, вы ввели не число")
else:
    index_list = []
    for i in range(len(input_list)):
        if min_num <= input_list[i] <= max_num:
            index_list.append(i)
    print("Список индексов: {}".format(index_list))
