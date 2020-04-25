import os


class MyClass:
	def __init__(self, x, y):  # Это конструктор
		self.num1 = x
		self.num2 = y

	def sum(self):
		numsum = self.num1 + self.num2
		return numsum


obj = MyClass(6, 7)
print(obj.sum())


# __call__ - срабатывает при вызове экземпляра класса.
class A:
	def __call__(self, z):
		return z * z


a = A()
print(a(8))


# __str__. Он вызывается, когда экземпляр класса должен быть
# представлен в виде строки.
class B:
	def __str__(self):
		return "z*6"


b = B()
print(b)


# super - главная задача это возможность использования
# в классе потомке, методов класса-родителя.
class A2:
	def __init__(self):
		print(u'конструктор класса A')


# Потомок класса А
class B2(A):
	def __init__(self):
		print(u'конструктор класса B')
		super(B2, self).__init__()


a = B2()


# Статические методы доступны без создания экземпляра класса
class AB:
	@staticmethod  # Указание на статичкий метод
	def mymethod(a, b):
		return a + b


print(AB.mymethod(12, 13))


# Документирование класса
class A3:
	"""Это строка документирования класса."""
	def test(self):
		"""Это документирование метода test"""
		pass


print(A3.__doc__)
print(A3.test.__doc__)

os.system("pause")
