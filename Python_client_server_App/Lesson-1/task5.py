"""
Задание 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтового в строковый тип на кириллице.
"""

import chardet   # необходима предварительная инсталляция: pip install chardet
import subprocess
import platform


input_web_resources = ('yandex.ru', 'youtube.com')


def web_ping(web):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', web]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


for i in input_web_resources:
    web_ping(i)
    print('-'*70)
