#函数
#定义： def 名称():  功能
import json
def say_hello():
    print("hello world")
say_hello()

#参数：
def say_hi(name):#形参
    print("hello, " + name)
say_hi("zhang")#实际参数

#多个参数可按顺序写，也可
def student(name,age):
    print("hello, " + name)
    print("age:", age)
student(age=18,name="zhang")
#也可def时给参数一个默认值，后面覆盖

#返回值
def add(a,b):
    return a+b
x=add(3,4)
print(x)
#return也会立即结束函数

#return多个值
def calculate(a,b):
    return a+b,a-b,a*b
print(type(calculate(3,4)))
print(calculate(3,4))

#局部变量，全局变量
#global x   x=  修改全局变量，少用

def get_level(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print(get_level(90))
print(get_level(80))

def calculate_average(scores):
    return sum(scores)/len(scores)

def find_student(scores,name):
    if name in scores:
        return scores[name]
    else:
        return None

#open()
file=open("student.txt","r",encoding="utf-8")
file.close()

#with open
with open("student.txt","r",encoding="utf-8") as f:
    content=f.read()

#写入
with open("scores.txt","w",encoding="utf-8") as f:
    f.write("1\n")

#读取全部
with open("scores.txt","r",encoding="utf-8") as f:
    cont=f.read()
print(cont)

#读取一行一次
with open ("student.txt","r",encoding="utf-8") as f:
    line=f.readline()
    print(line)

#读取全部行做列表
with open ("scores.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
print(lines)

#直接遍历
with open("students.txt","r",encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        print(line)

#JSON
import json
with open ("student.json","w",encoding="utf-8") as f:
    json.dump(scores,f,ensure_ascii=False,indent=4)

with open ("student.json","r",encoding="utf-8") as f:
    s=json.load(f)

#异常处理
def input_score():
    try :
        score=float(input("请输入成绩："))
    except ValueError:
        print("成绩必须是数字")
    if score<0 or score>100:
        print("输入范围错误")
    return score

