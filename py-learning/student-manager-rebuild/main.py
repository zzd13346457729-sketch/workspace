import json
DATA_NAME="./data/students.json"
def get_level(score):
    if score>=90:
        return("优秀")#
    elif score>=80:
        return("优良")#
    elif score>=70:
        return("良好")#
    elif score>=60:
        return("及格")#
    else:
        return("不及格")#

def load_students():
    try:
        with open(DATA_NAME,"r",encoding="utf-8") as f:
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
    
def save_students(students):
    try:
        with open(DATA_NAME,"w",encoding="utf-8") as f:
            json.dump(students,f,ensure_ascii=False,indent=4)
        return True
    except OSError as e:
        print(e)
        return False

def add_student(students):
    name=input("请输入姓名：")
    score=input("请输入分数：")
    if name in students:
        print("该学生已存在，是否要修改成绩？是请输入1，不是请输入0\n")
        a=input("请输入：")
        if a:
            students[name]=score
            print("修改成功")
        else:
            return 0
    else:
        if type(name)==str and type(score)==digit and score>=0 and score<=0:##
            students[name]=score
        else:
            print("请输入正确的学生姓名与成绩，分别为字符串与0-100的整数")
    
def check_student(students):
    name1=input("请输入要查询的学生姓名：")
    for name,score in students.items():
        if name==name1:
            print(f"姓名，{name}，分数，{score}，等级，{get_level(score)}")
        else:
            print("未查询到")

def show_all_students(students):
    if len(students) == 0:
        print("目前没有学生数据。")
        return
    for name,score in students.items():
        print(f"姓名，{name}，分数，{score}，等级，{get_level(score)}\n")

def delete_student(students):
    name1=input("请输入要删除的学生姓名：")
    for name,score in students.items():
            if name==name1:
                students.pop(name)
            else:
                print("该学生不存在，删除失败")

def calculate_average(scores):
    if len(scores)==0:
        return None#
    else:
        a=sum(scores)/len(scores)
        return a

def calculate_statistics(students):
    if len(students)==0:#
        return None,{}#
    dic={"优秀":0,"优良":0,"良好":0,"及格":0,"不及格":0}
    for score in students.values():
        dic[get_level(score)]+=1
    a=calculate_average(students.values())#
    #
    return a,dic


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
    students=load_students()
    while True:
        show_menu()
        choice = input("请选择功能：").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            check_student(students)
        elif choice == "3":
            show_all_students(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            calculate_statistics(students)
        elif choice == "0":
            print("程序已经退出。")
            break
        else:
            print("输入错误：请输入菜单中存在的选项。")


if __name__ == "__main__":
    main()
