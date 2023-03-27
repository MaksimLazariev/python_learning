"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

# Исходные слова
words = ['разработка', 'администрирование', 'protocol', 'standard']
print("Исходные слова:", *words, sep="\n")

encoding_words = []
decoding_words = []

# Переводим в байтовое представление
for word in words:
    encoding_words.append(word.encode('utf-8'))
print("\nСлова в байтовом представлении:", *encoding_words, sep="\n")

# Переводим в строчное представление
for word in encoding_words:
    decoding_words.append(word.decode('utf-8'))
print("\nСлова в строчном представлении:", *decoding_words, sep="\n")
