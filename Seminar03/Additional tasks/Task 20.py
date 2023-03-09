"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет
определенную ценность. В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите
программу, которая вычисляет стоимость введенного пользователем слова. Будем
считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.

*Пример:*

ноутбук
    12
"""

import re

"""
Решение:
1. Определяем язык
2. Запускаем функцию подсчета (русскую или английскую)
3. В функции сразу заводим словарь по буквам
"""


# Функция проверки текста, кириллица или нет
def is_cyrillic(input_text):
    return bool(re.search('[а-яА-Я]', input_text))


def english_count(input_text):
    # Английский словарь
    eng_alphabet = {1: 'AEIOULNSTR',
                    2: 'DG',
                    3: 'BCMP',
                    4: 'FHVWY',
                    5: 'K',
                    8: 'JX',
                    10: 'QZ'}
    # считаем сумму очков
    return sum(
        [k for i in input_text for k, v in eng_alphabet.items() if i in v])


def russian_count(input_text):
    # Русский словарь
    rus_alphabet = {1: 'АВЕИНОРСТ',
                    2: 'ДКЛМПУ',
                    3: 'БГЁЬЯ',
                    4: 'ЙЫ',
                    5: 'ЖЗХЦЧ',
                    8: 'ШЭЮ',
                    10: 'ФЩЪ'}
    # считаем сумму очков
    return sum(
        [k for i in input_text for k, v in rus_alphabet.items() if i in v])


# Вводим слово
word = input("Введите слово: ").lower()
if is_cyrillic(word):  # Проверка на кириллицу
    letter_sum = russian_count(word)
else:
    letter_sum = english_count(word)
if letter_sum:
    print("Вы получите {} очков".format(letter_sum))
else:
    print("Введено неверное слово")