from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name="MyPackage",
    version="1.0",
    description="Package Description",
    long_description=open(join(dirname(__file__), "README.md")).read(),
    url="http://example.com",
    packages=find_packages(),
    install_requires=[],  # Зависимости
    entry_points={  # Для выполнения командой mypckg в консоли
        "console_scripts": ["mypckg = module1.main:print_message"]
    },
)
