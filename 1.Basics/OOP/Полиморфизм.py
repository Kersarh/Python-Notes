import os

# Полиморфизм - это возможность использования одного и того же имени
# операции или метода к объектам разных классов.


class A:
	def oper(self, x, y):
		num = x + y
		return num


class B(A):  # Наследуем класс "А"
	def oper(self, x, y):  # <-----
		num = x / y
		return num


obj1 = A()
print(obj1.oper(2, 4))

obj2 = B()
print(obj2.oper(2, 4))

os.system("pause")
