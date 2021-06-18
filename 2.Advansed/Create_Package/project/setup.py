"""
setup.py - параметры для сборки пакетов
"""

# from setuptools import setup
from distutils.core import setup  # для whl
from os.path import dirname, join

from setuptools import find_packages

setup(
    name="MyPackage",
    version="1.0",  # Указать в файле __init__.py удалить здесь
    description="Package Description",
    long_description=open(join(dirname(__file__), "README.md")).read(),
    url="http://example.com",
    packages=find_packages(),
    include_package_data=True,  # Подключить файлы из MANIFEST.in
    install_requires=[],  # Зависимости
    entry_points={
        "console_scripts": ["mypckg = module1.main:print_message"]
        # Теперь можно вызвать mypckg в консоли.
        # Будет выполнен module1.main:print_message
    },
    test_suite="tests",  # Подключаем тесты 'python setup.py test'
)
