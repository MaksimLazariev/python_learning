"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X. Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих строках записаны N целых
чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

# Вводим количество элементов, массив и искомое число, сразу делаем валидацию
try:
    number_of_elements = int(input("Введите количество элементов в массиве: "))
    input_list = input("Введите список чисел через пробел: ").split()
    numbers_list = list(map(int, input_list))
    search_number = int(input("Введите искомое число: "))
except ValueError:
    print("Введены неверные данные")
else:   # Проверяем, чтоб число элементов совпадало с массивом
    if number_of_elements == len(numbers_list):
        min_diff = numbers_list[-1]
        # Находим самый близкий по значению элемент (модуль разности)
        for index in numbers_list:
            if abs(search_number - index) < min_diff:
                min_diff = search_number - index
        # Выводим результат, близкое к заданному и заданное число
        print("Число {} является самым близким к искомому {} ".format(
            search_number - min_diff, search_number))
    else:
        print("Количество введенных элементов не совпадает с массивом")
