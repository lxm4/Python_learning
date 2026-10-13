import json
from pathlib import Path

from Student import Student


class StudentCMS(object):
    def __init__(self, data_file=None):
        """
        该方法用于初始化学生管理系统对象的属性
        """
        self.data_file = Path(data_file) if data_file else Path(__file__).with_name("students.json")
        self.students = self._load_students()

    def _load_students(self):
        """
        从数据文件中读取学生信息，并转换为 Student 对象列表。

        如果数据文件不存在，说明系统还没有保存过学生信息，此时返回空列表。
        如果文件无法打开、JSON 格式错误或学生数据字段不完整，则打印提示信息，
        并返回空列表，避免程序因为数据文件问题而直接退出。

        :return: 读取到的 Student 对象列表；读取失败时返回空列表
        """
        if not self.data_file.exists():
            return []
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return [Student.from_dict(item) for item in data]
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("学生数据文件无法读取，将从空列表开始。")
            return []

    def _save_students(self):
        """
        将当前内存中的所有学生信息保存到数据文件。

        保存前会调用每个 Student 对象的 to_dict 方法，将对象转换为适合
        JSON 存储的字典。文件使用 UTF-8 编码，并保留中文字符和缩进格式，
        方便直接查看 students.json 文件中的内容。

        如果文件无法写入，则打印错误提示；该方法不向外抛出文件操作异常。
        """
        try:
            with self.data_file.open("w", encoding="utf-8") as file:
                json.dump(
                    [student.to_dict() for student in self.students],
                    file,
                    ensure_ascii=False,
                    indent=2,
                )
        except OSError:
            print("学生数据保存失败，请检查文件权限。")

    def add_student(self, student):
        """
        将一个新的学生对象添加到学生列表，并保存到数据文件。

        学生姓名不能为空，且不能与已有学生重名。只有通过这两项检查后，
        学生对象才会加入内存中的列表，并立即持久化到 students.json 文件。

        :param student: 学生对象
        :return: 添加成功返回 True；姓名为空或已存在时返回 False
        """
        if not student.name or any(item.name == student.name for item in self.students):
            return False
        self.students.append(student)
        self._save_students()
        return True

    def remove_student(self, name):
        """
        根据学生姓名查找并删除对应的学生对象。

        找到匹配的学生后，会从内存中的学生列表删除该对象，并立即保存
        最新数据；如果没有找到匹配姓名的学生，则不修改数据文件。

        :param name: 学生姓名
        :return: 删除成功返回 True；未找到学生时返回 False
        """
        for index, student in enumerate(self.students):
            if student.name == name:
                del self.students[index]
                self._save_students()
                return True
        return False

    def display_students(self):
        """
        在控制台中显示当前系统保存的所有学生信息。

        如果学生列表为空，则显示暂无学生信息的提示；否则依次调用每个
        Student 对象的字符串表示方法，将学生信息逐条打印出来。

        :return: 无返回值
        """
        if not self.students:
            print("暂无学生信息。")
            return
        for student in self.students:
            print(student)
    def show(self):
        """
        在控制台中显示学生管理系统的操作菜单。

        菜单列出添加、删除、查看学生和退出系统四个选项，供 main.py
        获取用户输入后执行对应的业务操作。本方法只负责显示菜单，不负责
        读取用户输入或处理菜单选择。

        :return: 无返回值
        """
        print("=" * 30)
        print("欢迎使用学生管理系统")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 显示所有学生")
        print("4. 退出系统")
        print("=" * 30)
        

        