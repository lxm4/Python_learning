"""
子类重写父类功能后继续访问父类功能：
    1. 通过父类名.方法名(self)的方式访问父类功能。精准访问，想找哪个就找哪个
    2. 通过super().方法名()的方式访问父类功能。访问最近的父类功能，有就用，没有就往后找

"""
class Animal:
    def eat(self):
        print("动物吃东西")
    
class Dog(Animal):
    def eat(self):
        print("狗吃骨头")
    
    def eat_from_parent(self):
        Animal.eat(self)  # 通过父类名访问父类方法

class Cat(Animal):
    def eat(self):
        print("猫吃鱼")
    
    def eat_from_parent(self):
        super().eat()  # 通过super()访问父类方法

if __name__ == "__main__":
    dog = Dog()
    dog.eat()  # 调用子类方法
    dog.eat_from_parent()  # 调用父类方法

    cat = Cat()
    cat.eat()  # 调用子类方法
    cat.eat_from_parent()  # 调用父类方法
