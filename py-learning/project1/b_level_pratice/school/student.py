from .grading import get_level


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_info(self):
        level = get_level(self.score)

        print(f"姓名：{self.name}")
        print(f"成绩：{self.score}")
        print(f"等级：{level}")
