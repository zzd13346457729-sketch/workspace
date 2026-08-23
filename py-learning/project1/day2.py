#字符串的三种定义方式
name="zzd"
print(type(name),name)
name=('yuanshen')
print(type(name),name)
name="""1"""
print(type(name),name)
name='''2
0
4
8'''
print(type(name),name)

#引号的嵌套
name=('"yuanshen')
name=("'yuanshen'")
print(type(name),name)
name=("\"yuanshen")
print(type(name),name)


home=("tangchenyipin")
name="zzd"
age="18"
#age=18 DONOT WORK +号连接需字符串
print("我是"+name+",我住在"+home+",我今年"+age)
print("我是%s" %name)
print("我是%s，今年%s岁，住在%s" %(name,age,home))
money=15000.1
age=18
print("我是%s, 我今年%d, 我有%f元" %(name,age,money))
print("我是%s, 我今年%0d, 我有%.1f元" %(name,age,money))
print("我是%s, 我今年%4d, 我有%.1f元" %(name,age,money))
#快速格式化
print(f"我是{name}，今年{age}，存款有{money}元")
#对表达式进行格式化
print("10+10=%d" %(10+10))
print(f"10*10={10*10}")
print("字符串的类型是：%s" %type("字符串"))


print("请输入你的账号:")
name=input()
print(f"你的账号是：{name}")
#更简洁
password=input("请输入你的密码：")
print("你的密码是：%s" %password)


password=int(password)
if password==123456:
    print("登录成功！")
elif password//10<=5:
    print("位数不够，请重试")
else:
    print("GUN")

while(password>0):
    if password==6:
        password-=1
        continue#结束本轮循环，开始下一次
    print(password)
    password-=10
    if password<5:
        break#终止循环


for i in range(5):
    print(i)

s="yuanshen"
for c in s:
    print(c)