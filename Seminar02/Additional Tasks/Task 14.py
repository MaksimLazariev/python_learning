"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
"""

number = int(input("Введите целое натуральное число: "))
# two_to_the_degree = 1
degree = 0
print("2 в степени, не превышающие {}".format(number))
while 2 ** degree < number:
    print("2 в степени {} равно {}".format(degree, 2 ** degree))
    degree += 1
