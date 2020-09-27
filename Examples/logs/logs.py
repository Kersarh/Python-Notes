'''
Логирование
'''
import logging

# Создаём logger
logger = logging.getLogger("example")
logger.setLevel(logging.DEBUG)

# Создаем handler и задаём уровень
handl = logging.StreamHandler()
handl.setLevel(logging.DEBUG)

# Задаем формат
formatter = logging.Formatter(
    "%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")

# Добавляем формат
handl.setFormatter(formatter)

# добавляем handl в наш logger
logger.addHandler(handl)

# Сообщение отладочное
logger.debug("Debug message")
# Сообщение информационное
logger.info("Info message")
# Сообщение предупреждение
logger.warning("Warning message")
# Сообщение ошибки
logger.error("Error message")
# Сообщение критическое
logger.critical("Critical message")
