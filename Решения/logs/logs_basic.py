import logging
import os
import sys

log1 = logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] # %(levelname)-8s # %(filename)s # [LINE:%(lineno)d] # %(message)s',
)  # Для вывода в файл filename=u'mylog.log'

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

os.system('pause' if os.name == 'nt'
          else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
