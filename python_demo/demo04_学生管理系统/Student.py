class Student:
    def __init__(self, name, gender, age, phone, desc):
        """
        该方法用于初始化学生对象的属性
        :param name: 学生姓名
        :param gender: 学生性别
        :param age: 学生年龄
        :param phone: 学生电话
        :param desc: 学生描述
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "phone": self.phone,
            "desc": self.desc,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["gender"],
            int(data["age"]),
            data["phone"],
            data["desc"],
        )

    def __str__(self):
        """
        该方法用于返回学生对象的字符串表示
        :return: 学生对象的字符串表示
        """
        return f"姓名：{self.name}, 性别：{self.gender}, 年龄：{self.age}, 电话：{self.phone}, 描述：{self.desc}"

if __name__ == "__main__":
    # 创建学生对象
    student1 = Student("张三", "男", 20, "1234567890", "优秀学生")
    student2 = Student("李四", "女", 19, "0987654321", "活泼开朗")

    # 打印学生对象的字符串表示
    print(student1)
    print(student2)