"""
Задание 1.
Реализовать дескрипторы для любых двух классов

Решение: в задаче реализованы два класса дескрипторов для валидации двух типов
данных: строковых и числовых


Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
str: str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""


# Вводим класс IsString для валидации str аргументов
class IsString:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Значение должно быть строкой")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя атрибута владельца - hours, rate
        self.my_attr = my_attr


# Вводим класс IsPositNum для валидации положительных аргументов
class IsPositNum:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Значение должно быть положительным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя атрибута владельца - hours, rate
        self.my_attr = my_attr


# Создаем класс Worker
class Worker:
    # Создаем дескрипторы
    name = IsString()
    surname = IsString()
    position = IsString()
    wage = IsPositNum()
    bonus = IsPositNum()

    # Производим валидацию значений аргументов
    def __init__(self, *args):
        self.name = args[0]
        self.surname = args[1]
        self.position = args[2]
        self.wage = args[3]
        self.bonus = args[4]
        self._income = {"wage": self.wage, "bonus": self.bonus}
        print("\nСоздан новый объект: {}, {}, {}, {}".format(self.name,
                                                             self.surname,
                                                             self.position,
                                                             self._income))

    # Перегрузка __str__ объекта
    def __str__(self):
        return "{} {}".format(self.name, self.surname)


# Создаем наследующий класс Position
class Position(Worker):

    # Задаем метод получения полного имени
    def get_full_name(self):
        return ' '.join([self.position, self.surname, self.name])

    # Задаем метод получения полного дохода
    def get_total_income(self):
        return sum(self._income.values())


# Объект класса Worker
wkr01 = Worker('Иван', 'Михайлов', 'механик', 6000, 5000)
print("Вывод перегрузки объекта через __str__ : {}".format(wkr01))

# # Пример 1, 1й аргумент число вместо строки
# wkr02 = Worker(100, 'Михайлов', 'механик', 6000, 5000)
# print("Вывод перегрузки объекта через __str__ : {}".format(wkr01))

# Пример 2, 4й аргумент отрицательный
wkr03 = Position('Алексей', 'Иванов', 'столяр', -7000, 8000)

print("Должность и ФИО сотрудника: {}".format(wkr03.get_full_name()))
print("Полный доход сотрудника равен {} руб".format(wkr03.get_total_income()))
