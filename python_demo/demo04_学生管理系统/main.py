from Student import Student
from StudentCMS import StudentCMS


def input_age():
    while True:
        age_text = input("请输入学生年龄: ").strip()
        if age_text.isdigit() and 0 < int(age_text) <= 150:
            return int(age_text)
        print("年龄必须是 1 到 150 之间的数字，请重新输入。")


def main():
    cms = StudentCMS()
    while True:
        cms.show()
        choice = input("请输入您的选择: ").strip()
        if choice == "1":
            name = input("请输入学生姓名: ").strip()
            gender = input("请输入学生性别: ").strip()
            age = input_age()
            phone = input("请输入学生电话: ").strip()
            desc = input("请输入学生描述: ").strip()
            student = Student(name, gender, age, phone, desc)
            if cms.add_student(student):
                print("学生添加成功。")
            else:
                print("添加失败：学生姓名不能为空或已存在。")
        elif choice == "2":
            name = input("请输入要删除的学生姓名: ").strip()
            if cms.remove_student(name):
                print("学生删除成功。")
            else:
                print("未找到该学生。")
        elif choice == "3":
            cms.display_students()
        elif choice == "4":
            print("感谢使用学生管理系统!")
            break
        else:
            print("无效的选择，请重新输入.")

if __name__ == "__main__":
    main()