from storage import read_students
from storage import save_students
def get_level(score):
    if score>=90:
        return("A")
    elif score>=80:
        return("B")
    elif score>=70:
        return("C")
    elif score>=60:
        return("D")
    else:
        return("NP")

def add_change_student(students):
    name=input("请输入姓名：").strip()
    if not name:
        print("姓名不能为空，请重新进入添加")##
        return 0##修改了print和return
    while True:
        try: 
            score=float(input("请输入分数：").strip())
            if not (0<=score<=100):##NaN
                print("范围错误，请输入零到一百的数字")
                continue
            break
        except ValueError as e:
            print(f"{e}，请输入数字，请重试")
            continue
    #if students.get(name):##改为name in students 0分会False
    if name in students:    
        print("该学生存在，是否修改ta的成绩？\n是请输入yes，否请输入no")
        while True:##添加了循环防止输错
            yn=input().strip().lower()
            if yn=="yes":
                students[name]=score
                break
            elif yn=="no":
                return 0
            else:
                print("输入错误,请重试,输入yes 或 no")
                continue
    else:
        students[name]=score

def find_student(students):
    name=input("请输入要查询的学生姓名：").strip()
    #if not students.get(name):
    if name not in students:
        return("未找到该学生")
    else:
        return(f"姓名：{name}  成绩：{students[name]}  等级：{get_level(students[name])}")

def showcase_all(students):
    if not students:
        print("暂无记录的学生与成绩")
        return 0
    else:
        for name,score in students.items():
            print(f"姓名：{name}，成绩：{score}，等级：{get_level(score)}\n")
#修改return成为print

def remove_student(students):
    name=input("请输入要删除的学生姓名：").strip()
    if name not in students:
    ##if not students.get(name):##改为name in students 0分会False
            print("未找到该学生，请重试")
            return 0
    else:
            students.pop(name)

def show_statistics(students):
    if not students:##判断往前放，后面的else删去
        return None,{}##修改return
    sum=0
    s=0
    level_dic={"A":0,"B":0,"C":0,"D":0,"NP":0}
    for i in students.values():
        sum+=i
        s+=1
        a=get_level(i)
        level_dic[a]+=1
    aver=sum/s
    return aver,level_dic

def show_menu():
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加/修改学生")
    print("2. 查询学生")
    print("3. 显示全部")
    print("4. 删除学生")
    print("5. 平均成绩与等级统计")
    print("0. 退出程序")

def main():
    students=read_students()
    if students is None:
        return
    while True:
        show_menu()
        select=input("请输入:")
        if select=="1":
            add_change_student(students)
        elif select=="2":
            result=find_student(students)
            print(result)
        elif select=="3":
            showcase_all(students)
        elif select=="4":
            remove_student(students)
        elif select=="5":
            ##a,b=show_statistics(students)
            ##print(a)
            ##print(b)
            average, level_counts = show_statistics(students)
            if average is None:
                print("暂无数据，请添加")
            else:
                print(f"平均分：{average:.2f}")
                print(level_counts)
        elif select=="0":
            print("已退出")
            break
        else:
            print("输入错误，请重试，输入0-5")
            continue
        save_students(students)

if __name__ == "__main__":
    main()