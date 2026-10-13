"""
单继承与多继承
单继承与多继承
案例：演示一个字类继承自一个父类
案例：演示一个字类继承自多个父类
"""
class Parent1:
    def method1(self):
        print("Parent1 method1")

class Parent2:
    def method1(self):
        print("Parent2 method2")

class Child(Parent2):
    pass

class Child1(Parent1, Parent2):#从左到右，就近原则，同一方法优先调用第一个父类的方法
    pass

child = Child()
child.method1()  # 调用父类Parent2的方法
child1 = Child1()
child1.method1()  # 调用父类Parent1的方法
print(Child1.__mro__)  # 查看类的继承顺序 child1->Parent1->Parent2->object

