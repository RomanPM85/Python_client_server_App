words_str = ('разработка', 'сокет', 'декоратор')
words_utf = ('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
             '\u0441\u043e\u043a\u0435\u0442',
             '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')


def print_str(words):
    for i in words:
        print(i)
        print(type(i))


print_str(words_str)
print_str(words_utf)
