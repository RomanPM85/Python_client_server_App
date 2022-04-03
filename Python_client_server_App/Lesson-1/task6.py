"""
Задание 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед
нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке
он был создан.
"""

import random
from chardet import detect

# Вводные данные
input_words_str = ('сетевое программирование', 'сокет', 'декоратор')
output_file = 'test_file.txt'
list_codings = ['utf-8', 'utf-16', 'utf-32']
random_element = random.choice(list_codings)

# 1. создаём файл в заданной кодировке
f = open(output_file, 'w', encoding=random_element)
for line in input_words_str:
    f.write(line + '\n')
f.close()

# 2. узнаём кодировку неизвестного нам файла
with open(output_file, 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)

# 3. Теперь открываем файл в УЖЕ известной нам кодировке
with open(output_file, encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
    print()
