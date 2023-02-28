# Задание 3.
#
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

input_number = input('Введите число: ')  # вводное число
raise_number = input_number  # растущее число
summa = 0  # сумма вначале равна 0
count = 3  # сколько раз увеличиваем число

for i in range(count):
    summa += int(raise_number)  # увеличиваем сумму
    raise_number += input_number  # приписываем исходное число к растущему
print(f'Сумма равна {summa}')  # вывод суммы
