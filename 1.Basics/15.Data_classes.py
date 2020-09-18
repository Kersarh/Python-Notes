'''
Классы данных (Data classes) - Одна из возможностей появившихся в Python 3.7. Они призваны автоматизировать генерацию кода классов, которые используются для хранения данных.
'''

from dataclasses import dataclass


class name:
    def __init__(self, name: str, age: int = 10):
        self.name = name
        self.age = age

    def prnt_data(self) -> float:
        print(self.name, self.age)


name = name("user", 20)
name.prnt_data()  # user 20
print(name)  # <__main__.name object at 0x000001C87ED0A610>
print("---------------------")


#  с применением dataclass:
@dataclass
class name2:
    name: str
    age: int = 10

    def prnt_data(self) -> float:
        print(self.name, self.age)


name = name2("user", 20)  # user 20
name.prnt_data()  # name2(name='user', age=20)
print(name)
print("---------------------")
