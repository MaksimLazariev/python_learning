"""
Задача 3.
Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно
быть два элемента — номер товара и словарь с параметрами (характеристиками
товара: название, цена, количество, единица измерения). Структуру нужно
сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


def goods_data_input(goods_num):
    """
    Функция для ввода списка кортежей «Товары».

    :goods_num: переменная обозначает, какое количество товаров будем вводить
    :return: возвращаем готовый список кортежей
    """

    input_list = []
    for count in range(1, goods_num + 1):
        # Заполняем словарь для count элемента
        input_dict = {
            "название": input("\nВведите название {} товара: ".format(count)),
            "цена": int(input("Введите цену {} товара: ".format(count))),
            "количество": int(
                input("Введите количество {} товара: ".format(count))),
            "ед": input("Введите единицу измерения {} товара: ".format(count))}
        # Присоединяем к списку элемент как кортеж count и полученного словаря
        input_list.append((count, input_dict))
    return input_list


def convert_list_to_dict(input_list):
    """
    Функция для перевода списка кортежей в словарь списков и сортировка
    значений по ключам.

    :input_list: исходный список кортежей
    :return: возвращаем готовый словарь списков
    """
    # Заводим пустой словарь
    result_dict = {'название': [], 'цена': [], 'количество': [],
                   'ед': set()}
    # Заполняем словарь из списка согласно значениям ключей
    for l_keys, l_values in input_list:
        result_dict['название'].append(l_values['название'])
        result_dict['цена'].append(l_values['цена'])
        result_dict['количество'].append(l_values['количество'])
        result_dict['ед'].add(l_values['ед'])
    # Возвращаем словарь
    return result_dict


# Вводим количество товаров
try:
    goods_number = int(input("Сколько наименований товаров будем вводить? "))
except ValueError:
    print("Введены неверные данные")
else:
    # Заполняем список с помощью функции goods_data_input
    goods_list = goods_data_input(goods_number)
    # Печать заполненного списка
    print("\nПолученный список-словарь:")
    for keys, values in goods_list:
        print("({}, {})".format(keys, values))
    # Запоняем словарь с помощью функции convert_list_to_dict
    analytics_dict = convert_list_to_dict(goods_list)
    # Печать полученного словаря
    print("\nПолученный словарь-аналитика:")
    for keys, values in analytics_dict.items():
        print("('{}': {})".format(keys, values))
