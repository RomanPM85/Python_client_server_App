"""Константы"""

import logging

DEFAULT_PORT = 7777  # Порт по умолчанию для сетевого взаимодействия
DEFAULT_IP_ADDRESS = '127.0.0.1'  # IP адрес по умолчанию для подключения клиента
MAX_CONNECTIONS = 5  # Максимальная очередь подключений
MAX_PACKAGE_LENGTH = 1024  # Максимальная длинна сообщения в байтах
ENCODING = 'utf-8'  # Кодировка проекта
LOGGING_LEVEL = logging.DEBUG  # Текущий уровень логирования
ACTION = 'action'  # Протокол JIM основные ключи:
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
PRESENCE = 'presence'  # Прочие ключи, используемые в протоколе
RESPONSE = 'response'
ERROR = 'error'
RESPONSE_DEFAULT_IP_ADDRESS = 'response_default_ip_address'
