"""
类外设置对象的属性，格式如下：
    对象名.属性名=属性值
    特点：该属性独属于此对象，即该类的其他对象没有这个属性

类外获取对象的属性
    对象名.属性名

类 = 创建对象的模板/类型，同时它本身也是一个对象。
实例 = 根据这个类创建出来的具体对象。
"""
class Car:
    def run(self):
        print(f'汽车会跑')

c1=Car()
c1.run()
c1.color='red'
c1.number=4
print(f'{c1.color}')
print(f'{c1.number}')
print('-'*20)
c2=Car()
c2.run()