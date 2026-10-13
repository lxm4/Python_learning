"""
对象属性：属于每个对象的，即：每个对象的属性都可能不同。修改A的属性不会影响B的属性。
类属性：属于类的，即：所有对象共享同一个属性。修改类属性会影响所有对象的属性。

对象属性：
    定义到init方法中，属于每个对象的属性
    只能通过对象名.的方式访问
类属性：
    定义到类中，属于类的属性，能被所有对象共享
    可以通过类名.或对象名.的方式访问，推荐使用类名.的方式
    只能通过类名.的方式修改，不能通过对象名.的方式修改
"""


class Student:
    # 类属性：所有学生对象共享同一个学校名称。
    school = "Python 学院"

    def __init__(self, name, age):
        # 对象属性：每个学生对象都有自己独立的姓名和年龄。
        self.name = name
        self.age = age


if __name__ == "__main__":
    student_a = Student("小明", 18)
    student_b = Student("小红", 19)

    # 对象属性彼此独立，修改小明的年龄不会影响小红。
    student_a.age = 20
    print(f"{student_a.name}：{student_a.age} 岁")
    print(f"{student_b.name}：{student_b.age} 岁")

    # 类属性可以通过类名访问，所有对象都能读取到修改后的值。
    print(f"修改前的学校：{Student.school}")
    Student.school = "Python 高级学院"
    print(f"{student_a.name} 的学校：{student_a.school}")
    print(f"{student_b.name} 的学校：{student_b.school}")

    # 通过对象名赋值会创建同名的对象属性，不会修改类属性。
    student_a.school = "小明自己的学校"
    print(f"{student_a.name} 的学校：{student_a.school}")
    print(f"{student_b.name} 的学校：{student_b.school}")
    print(f"类属性 school：{Student.school}")

