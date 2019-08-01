import logging
import logging.handlers
import os
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] # %(levelname)-8s # %(filename)s # [LINE:%(lineno)d] # %(message)s',
    filename='mylog.log'
)  # Для вывода в файл filename=u'mylog.log'

a = 10
b = 20
logging.warning('Summ {}+{}'.format(a, b))
print("a+b={}".format(a+b))


# Сообщение отладочное
logging.debug('Debug message')
# Сообщение информационное
logging.info('Info message')
# Сообщение предупреждение
logging.warning('Warning message')
# Сообщение ошибки
logging.error('Error message')
# Сообщение критическое
logging.critical('Critical message')
