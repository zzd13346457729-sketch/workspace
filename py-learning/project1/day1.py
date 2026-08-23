print("你好")
print(1)

name=input('请输入：')
print('hello,',name)
print(name,name,name)

print(666)
print(5.20)
print("学python")

'''
变量只能以字母与下划线开头，
只能由字母，数字与下划线组成，
区分大小写，
不能是关键字和保留字，
应具有描述性
'''

print(type(666))
print(type(5.20))
print(type("学python"))
#or
a=type(666)
b=type(5.20)
c=type("学python")
print(a)
print(b)
print(c)
#or
d=5.2
print(type(d))

#数据类型转换
a=str(666)
print(a)
b=int(5.60)
print(b)
#c=float("学python")
#print(c)  DONOT WORK!
#but
c=float("666")
print(c)
#can work

"""
运算符： + - * / // % **
+= -= *= /= //= %= **=
"""

a=4
print(a)
a+=3
print(a)
a-=5
print(a)
a*=4
print(a)
a//=3
print(a)
b%=2
b=a*3
print(b)
b**=3
print(b)