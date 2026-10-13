"""
__dict__属性介绍：
    它是python内置的属性，可以把对象转化成字典形式

对象转字典：my_dict = s1.__dict__
字典转对象：s1 = Student(**my_dict)
"""

from Student import Student


# 创建一个学生对象
student1 = Student("张三", "男", 20, "1234567890", "优秀学生")
print("原始对象：", student1)
print(type(student1))
# 使用 __dict__ 将对象转换成字典
student_dict = student1.__dict__
print("对象转成字典：", student_dict)


# 使用 ** 将字典拆包，传给 Student 的构造方法，重新创建对象
student2 = Student(**student_dict)
print("字典还原成对象：", student2)

# 修改字典后再创建对象，可以得到不同的学生对象
student_dict["name"] = "李四"
student_dict["age"] = 19
student3 = Student(**student_dict)
print("修改字典后创建的对象：", student3)
