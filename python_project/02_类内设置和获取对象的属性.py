"""
self.属性名
魔法方法：
    特点：Python 内置的函数，在满足特定条件时会自动被调用。

__init__：创建对象时自动调用，一般用于初始化对象的属性。

__str__：使用 print() 打印对象时自动调用，一般用于返回有意义的字符串信息。

__del__：对象被删除时自动调用，一般用于释放对象占用的资源。
"""


class Car:
    def __init__(self, color, number):
        """创建汽车对象时，初始化汽车的属性。"""
        print('__init__ 被调用')
        self.color = color
        self.number = number

    def __str__(self):
        """定义 print(对象) 时显示的内容。"""
        return f'这是一辆{self.color}的汽车，有{self.number}个轮子'

    def __del__(self):
        """删除对象时自动调用。"""
        print(f'{self.color}汽车被删除，__del__ 被调用')


car1 = Car('红色', 4)
print(car1.color)
print(car1.number)

print(car1)

car2 = Car('蓝色', 4)
print(car2)

del car1
del car2
