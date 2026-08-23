#索引 s[n] s[0] s[-1]
#切片 s[start:end:step]  [start,end)中每|step|个元素取一个,step为正则取左一，负为右一
#大小写转换，只有首字母大写
s="i have a dream"
s1=s.capitalize()
print(s1)
#标题化 即所有首字母大写
s2=s.title()
print(s2)
#全部字母小写
s3=s2.lower()
print(s3)
#全部字母大写
s4=s3.upper()
print(s4)
#忽略大小写
#验证码与输入的都变成大写或者小写即可比较
#strip
s="     你好啊，我叫周润发  "
print(s.strip())
#replace
print(s.replace(" ",""))
#split
s="python-java-c-javascript"
lst=s.split("-")
print(lst)
#join
s1="_".join(lst)
print(s1)
#find
s="你好啊，我叫周润发"
print(s.find("周润发"))
print(s.find("周润发123"))
#index
print(s.index("周润发"))
#print(s.index("周润发1"))
#startswith endswith isdigit isdecimal
name=input("请输入你的名字：")
if name.startswith("公孙"):
    print("Yes")
name2=input("请输入你的名字：")
if name2.endswith("诺"):
    print("Yes")
money=input("请输入money：")
if money.isdigit():
    print("Yes")
elif money.isdecimal():
    print("Yes")
else:
    print("No")
#len
print(len(money))
#in
print("诺"in money)
for i in s:
    print(i)