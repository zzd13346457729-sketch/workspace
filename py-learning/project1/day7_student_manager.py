import json
DATA_FILE = "./data/students.json"

def get_level(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

def calculate_average(scores):
    if len(scores)==0:
        return None
    else:
        return sum(scores)/len(scores)

def calculate_statistics(students):
    if len(students)==0:
        return None,{}
    scores=students.values()
    average=calculate_average(scores)
    level_counts={
        "A":0,
        "B":0,
        "C":0,
        "D":0,
        "F":0
    }
    for score in scores:
        level_counts[get_level(score)]+=1
    return average,level_counts

def load_students(filename=DATA_FILE):
    try:
        with open(filename,"r",encoding="utf-8") as f:
            students=json.load(f)
        if not isinstance(students,dict):
            raise ValueError
        return students
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("警告，数据文件格式损坏，将暂时使用空数据")
        return {}
    except ValueError as e:
        print(e)
        return {}
    except OSError as e:
        print(e)
        print("读取文件失败")
        return {}

def save_students(students,filename=DATA_FILE):
    try:
        with open(filename,"w",encoding="utf-8") as f:
            json.dump(students,f,ensure_ascii=False,indent=4)
        return True
    except OSError as e:
        print(e)
        return False

def input_score():
    while True:
        text=input("请输入成绩(0-100)：").strip()
        try:
            score=float(text)
        except ValueError:
            print("成绩必须是数字")
            continue
        if score<0 or score>100:
            print("请输入0-100间的数字")
            continue
        return score

def add_student(students):
    name=input("请输入姓名：").strip()
    if name =="":
        print("失败，姓名不能为空")
        return
    if name in students:
        print("失败，学生已存在")
        return
    score=input_score()
    students[name]=score
    if save_students(students):
        print(f"添加成功：{name}，成绩：{score:g}")
    else:
        students.pop(name)
        print("添加失败，数据未能保存")

def query_student(students):
    """按照姓名查询学生。"""
    name = input("请输入要查询的学生姓名：").strip()
    score = students.get(name)

    if score is None:
        print("没有找到该学生。")
        return

    level = get_level(score)
    print(f"姓名：{name}")
    print(f"成绩：{score:g}")
    print(f"等级：{level}")


def display_all(students):
    """显示所有学生。"""
    if len(students) == 0:
        print("目前没有学生数据。")
        return

    print("\n全部学生：")

    for name, score in sorted(students.items()):
        level = get_level(score)
        print(f"{name}：{score:g} 分，等级 {level}")


def delete_student(students):
    """删除一名学生。"""
    name = input("请输入要删除的学生姓名：").strip()

    if name not in students:
        print("删除失败：没有找到该学生。")
        return

    deleted_score = students.pop(name)

    if save_students(students):
        print(f"已经删除学生：{name}。")
    else:
        # 保存失败时恢复被删除的数据
        students[name] = deleted_score
        print("删除失败：数据未能保存。")


def show_statistics(students):
    """显示平均成绩和等级人数。"""
    average, level_counts = calculate_statistics(students)

    if average is None:
        print("目前没有成绩，无法统计。")
        return

    print(f"学生人数：{len(students)}")
    print(f"平均成绩：{average:.2f}")

    print("等级统计：")
    for level in ["A", "B", "C", "D", "F"]:
        print(f"{level}：{level_counts[level]} 人")


def show_menu():
    """显示主菜单。"""
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 显示全部")
    print("4. 删除学生")
    print("5. 平均成绩与等级统计")
    print("0. 退出程序")


def main():
    """程序主函数。"""
    students = load_students()

    while True:
        show_menu()
        choice = input("请选择功能：").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            query_student(students)

        elif choice == "3":
            display_all(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            show_statistics(students)

        elif choice == "0":
            print("程序已经退出。")
            break

        else:
            print("输入错误：请输入菜单中存在的选项。")


if __name__ == "__main__":
    main()