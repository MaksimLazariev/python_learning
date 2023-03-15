"""
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


# Создаем класс Worker
class Worker:

    # Задаем публичные параметры и выводим данные созданного объекта
    def __init__(self, *args):
        self.name = args[0]
        self.surname = args[1]
        self.position = args[2]
        self._income = {"wage": args[3], "bonus": args[4]}
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

    # Перегрузка __repr__ объекта
    # def __repr__(self):
    #     return "{}: {}".format(self.__class__, self.name)


# Объект класса Worker
wkr01 = Worker('Иван', 'Михайлов', 'механик', 6000, 5000)
print("Вывод перегрузки объекта через __str__ : {}".format(wkr01))

# Объект класса Position
wkr02 = Position('Алексей', 'Иванов', 'столяр', 7000, 8000)

print("Должность и ФИО сотрудника: {}".format(wkr02.get_full_name()))
print("Полный доход сотрудника равен {} руб".format(wkr02.get_total_income()))
