"""
类方法：
    属于类的方法，可以通过类名.的方式调用，也可以通过实例对象.的方式调用。
    定义类的方法的时候，需要使用@classmethod装饰器来修饰方法，
    并且第一个参数必须是cls，表示类本身。

静态方法：
    属于类的方法，可以通过类名.的方式调用，也可以通过实例对象.的方式调用。
    定义类的方法的时候，需要使用@staticmethod装饰器来修饰方法，参数传不传都可以

区别：
    1.类方法的第一个参数是cls，表示类本身，可以访问类的属性，静态方法无参数的特殊要求
    2.可理解为：类方法是类的行为，静态方法是类的工具，如果函数中要使用类对象就定义成类方法
    否测就定义成静态方法，除此外无区别

"""


class Student:
    school = "Python 学院"
    student_count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.student_count += 1

    @classmethod
    def show_school(cls):
        """类方法：通过 cls 访问类属性。"""
        print(f"学校：{cls.school}")
        print(f"学生人数：{cls.student_count}")

    @staticmethod
    def is_valid_score(score):
        """静态方法：只处理传入的数据，不依赖类属性或实例属性。"""
        return 0 <= score <= 100


student_a = Student("小明", 88)
student_b = Student("小红", 95)

# 类方法可以通过类名调用，也可以通过实例调用
Student.show_school()
student_a.show_school()

# 静态方法也可以通过类名调用，适合作为类相关的工具函数
print(f"{student_a.name} 的成绩是否有效：{Student.is_valid_score(student_a.score)}")
print(f"105 分是否有效：{Student.is_valid_score(105)}")
