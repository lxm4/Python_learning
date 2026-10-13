from abc import ABC, abstractmethod


class Animal(ABC):
	"""抽象类：规定所有动物都必须实现 eat 方法。"""

	@abstractmethod
	def eat(self):
		"""抽象方法：只规定接口，不提供具体实现。"""
		pass


class Dog(Animal):
	def eat(self):
		print("狗吃骨头")


class Cat(Animal):
	def eat(self):
		print("猫吃鱼")


if __name__ == "__main__":
	# 抽象类不能直接创建对象。
	try:
		Animal()
	except TypeError as error:
		print(f"Animal 不能直接实例化：{error}")

	# 子类实现了抽象方法后，就可以创建对象。
	dog = Dog()
	cat = Cat()
	dog.eat()
	cat.eat()
