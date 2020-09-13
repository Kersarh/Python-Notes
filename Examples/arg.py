#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import argparse

version = "1.0.0(beta)"

# Создаем парсер
parser = argparse.ArgumentParser(
    prog="program_name",
    description="""Описание программы""",
    epilog=""" (c) 2019. Автор программы, как всегда,
не несет никакой ответственности ни за что.""",
    add_help=False,
)

# Создаем группу параметров для основного парсера,
main_group = parser.add_argument_group(title="Параметры")
main_group.add_argument("--help", "-h", action="help", help="Справка")
main_group.add_argument(
    "--version",
    "-V",
    action="version",  # из переменной version
    help="Версия",
    version="%(prog)s {}".format(version),
)

# Создаем группу подпарсеров
subparsers = parser.add_subparsers(
    dest="test_command",
    title="Команды",
    description="Команды, передаются 1 параметром %(prog)s",
)
# Создаем парсер для команды test
test_parser = subparsers.add_parser(
    "test",
    add_help=False,
    help='Запуск в режиме "test"',
    description="""Запуск программы с параметром test""",
)

# Будет использована стандартная справка
parser.add_argument("-n", "--name", default="NAME", help="Имя пользователя")
parser.add_argument("-d", "--digit", default="1", type=int, help="Число")

# Возможные варианты команд
namespace = parser.parse_args(sys.argv[1:])
print(namespace)
print("Привет, {}! Число = {}, {}".format(namespace.name, namespace.digit,
                                          namespace.test_command))

os.system("pause" if os.name == "nt" else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
