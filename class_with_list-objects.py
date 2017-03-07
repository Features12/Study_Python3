def square(arg): # обычная функция 
	return arg ** 2


class Sum:
	def __init__(self, val):
		self.val = val
	def __call__(self, arg): # при обращнии к экземпляру, как к функции, вызовется
		return self.val + arg


class Product:
	def __init__(self, val):
		self.val = val
	def method(self, arg): # стандартный связанный метод
		return self.val * arg


class Negate:
	def __init__(self, val):
		self.val = - val
	def __repr__(self):
		return str(self.val) # вернет в str представлении 5


obj1 = Sum(2) # экземпляр + __init__
obj2 = Product(3)

actions = [square, obj1, obj2.method, Negate] # заключаем функцию и экземпляры, класс в список

a = [i(5) for i in actions]

