# Задание 3. Создать список и заполнить его элементами различных типов данных.
# Реализовать проверку типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно,
# в программе.
#
# Пример:
# для списка [5, "string", 0.15, True, None]
# результат
#
# <class 'int'>
# <class 'str'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

my_list = [5, "string", 0.15, True, None]  # Вводим список

for i in range(len(my_list)):  # Пробегаемся по всей длине списка
    print(type(my_list[i]))  # Печатаем каждый элемент списка