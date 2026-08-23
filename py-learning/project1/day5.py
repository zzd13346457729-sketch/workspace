#列表 有序记录可变数据
#元组 有序不可变
#集合 无序不重复
#字典 无序k-v集合

#元组tuple
#不可改变的列表
#可索引切片可for
#不可增删改

#单个字母，字符串组成的元组不能这样写：t=("1")
#正确写法：
t=("1",)
a=(1,)
print(t,a)

#集合set
#无序不重复
s={}
print(type(s))
s={1,2,3}
print(type(s))
#不能往里放不可哈希的数据类型如列表

#空集合s=set()
#类似的lst=list() s=str()

#添加元素
s.add(4)
print(s)

#删除
s.pop()
print(s)
#pop随机删除，不常用
s.add(5)
print(s)
s.remove(5)
print(s)
#remove常用

#改：先删再加

#查：
print(s)
for i in s:
    print(i)
#无序只能这样查

#交并差集
s2={1,2,8}
print(s&s2)
#交集
print(s|s2)
#补集
print(s^s2)
#并减交
print(s-s2)
#差集

#字典dict
#无序可变kv集合
d={"k1":"v1","k2":"v2","k3":"v3"}
w=d["k1"]
print(w)

#增删改查
#增加
d["jay"]="周杰伦"
d[1]=123
print(d)

#删除
d.pop(1)
print(d)

#改
d["jay"]="zhou"
print(d)

#查
print(d["jay"])
print(d.get("jay"))

#循环与嵌套

#用for可以拿到key
for i in d:
    print(i)
#or
for i in d.keys():
    print(i)
lst=list(d.keys())

#拿到value
print(d.values())

#拿到kv对
print(d.items())
for i in d.items():
    print(i)
#or
for k,v in d.items():
    print(k,v)

#嵌套
#eg.  a=wang[wife][assistant][name]

#循环删除
#字典不能在迭代中改变长度
temp=[]
for i in d:
    if i.startswith("j"):
        temp.append(i)
for i in temp:
    d.pop(i)
print(d)
