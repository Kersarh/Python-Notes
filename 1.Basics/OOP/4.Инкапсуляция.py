"""
Инкапсуляция — это связывание код и данные в оболочку, и сохраняет их в безопасности
как от изменения извне так и от ошибочного использования.
В ООП в роли оболочки выступают классы: 
они собирают данные и методы в одном месте,
а также защищают их от изменения извне(сокрытие).

Сокрытие является элементом инкапсуляции и обеспечивает
ограничение доступа к данным и методам,
что делает некоторые компоненты доступными только внутри класса.

Python предоставляет 3 уровня доступа к данным:
Публичный (public) - нет особого синтаксиса.
Приватный (private) - два нижних подчеркивания в начала названия.
Защищенный (protected) - одно нижнее подчеркивание в начале названия. Используется очень редко.
"""

# Класс А инкапсулярует данные и методы
class A:
    _i = 5

    def prnt(self):
        print("Public")

    # _ или __ разный уровень доступа
    def _fun1(self):
        print("protected")

    def __fun2(self):
        """Этот метод виден только мотодам внутри класса"""
        print("private")


a = A()
a.prnt()
a._fun1()
# a.__fun2() # Вызоыет ошибку так как нет доступа
