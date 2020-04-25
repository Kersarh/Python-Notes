import os
# --- Наследование ---


class A:
	def prt_a(self):
		print("class A")


class B(A):
	def prt_b(self):
		print("class B")


b = B()
b.prt_a()
b.prt_b()


# Множественно наследование
class Base1:
	def basemethod(self):
		return "Hello"


class Base2:
	value = 44


class MyClass(Base1, Base2):
	def __init__(self):
		self.a = 10


obj = MyClass()
print(obj.value)
print(obj.basemethod())

os.system("pause")
