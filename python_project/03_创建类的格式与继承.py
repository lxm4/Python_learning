"""
格式1:
    class 类名：

格式2:
    class 类名（）：

格式3:
    class 类名（object）：


继承：子类可以继承父类的属性与行为
写法：class 子类名（父类名）：
好处：
    1. 提高代码的复用性
    2. 提高代码的可维护性
弊端：
    1. 增加了代码的复杂性
    2. 可能导致类层次结构过于复杂
    3. 耦合性过高，父类不好的内容，子类想没有都不行
扩展：开发原则
    高内聚，低耦合
    内聚：一个类的功能越单一，内聚性就越高，指的是类自己独立处理问题的能力
    耦合：类与类之间的依赖关系，耦合性越低，类与类之间的依赖关系就越少
    依赖：一个类需要另一个类来完成其功能时，就产生了依赖关系
    大白话：自己能搞定的事情不要麻烦别人
"""

class Father(object):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.name}")

class Son(Father):
    pass

s=Son("Tom")
s.say_hello()  # 输出: Hello, I am Tom


