"""
Задание 1.
Реализовать дескрипторы для любых двух классов

Решение: в задаче реализован класс дескрипторов для валидации числовых данных

Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв.
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


# Вводим класс NonNegative для валидации аргументов
class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя атрибута владельца - hours, rate
        self.my_attr = my_attr


# Создаем класс
class Road:
    # Задаем дескрипторы
    mass = NonNegative()
    thickness = NonNegative()
    _length = NonNegative()
    _width = NonNegative()

    # Задаем значения аргументов и производим валидацию через дескрипторы
    def __init__(self, length=1000, width=10, mass=25, thickness=0.05):
        self._length = length
        self._width = width
        self.mass = mass
        self.thickness = thickness
        print("Создан новый объект размером {} м на {} м".format(self._length,
                                                                 self._width))

    # Задаем метод расчета массы куска дороги
    def get_weight(self):
        weight = self._length * self._width * self.mass * self.thickness
        print("Масса полотна равна: \n{}м*{}м*{}кг*{}м = {} кг = {} т".format(
            self._length, self._width, self.mass, self.thickness, weight,
            weight / 1000))


# Создаем 1‑й объект класса Road и расчитываем массу
rd01 = Road(5000, 20)
rd01.get_weight()

# Создаем 2‑й объект класса Road и расчитываем массу
rd02 = Road(10000, 50)
rd02.get_weight()

# Создаем 3‑й объект класса Road с параметрами по умолчанию и расчитываем массу
rd03 = Road()
rd03.get_weight()

# Изменяем массу на кг и толщину асфальта и расчитываем массу
rd03.mass = -50
rd03.thickness = 0.1
rd03.get_weight()
