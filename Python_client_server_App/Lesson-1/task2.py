"""
Задание 2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо
в автоматическом, а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае
не используя методы encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.
"""

input_words_str = ('class', 'function', 'method')


def b_str(words):
    """
    Функция, которая добавляет литеры b к текстовому значению
    и определить тип, содержимое и длину соответствующих переменных.
    """
    for i in words:
        text_merge = f"b'{i}'"
        print(type(eval(text_merge)))
        print(eval(text_merge))
        print(len(text_merge))

    print('-' * 70)


b_str(input_words_str)
