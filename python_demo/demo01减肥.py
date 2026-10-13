class Student:
    def __init__(self):
        self.current_weight = 100

    def run(self):
        print("疯狂跑步中...")
        self.current_weight -= 0.5
        print(f'跑步后体重为{self.current_weight}kg')

    def eat(self):
        print("疯狂吃东西中...")
        self.current_weight += 2
        print(f'吃东西后体重为{self.current_weight}kg')

    def __str__(self):
        return f'当前体重为{self.current_weight}kg'


xm=Student()
xm.eat()
xm.run()
xm.run()
print(xm)