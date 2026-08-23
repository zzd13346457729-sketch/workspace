#列表
#特性：可索引可切片，可for
#增删改查
#小项目：改张为王
lst=["张玉凤","张则栋","张之洞","林丹"]
#for i in lst:
 #   if i.startswith("张"):
 #       new1="王"+i[1:]
 #       i=new1
        #DON'T WORK
        #i只是暂时修改，不能修改到列表里
for i in range(0,4):#range(len(lst))更好
    if lst[i].startswith("张"):
        lst[i]="王"+lst[i][1:]
print(lst)
#排序
#升序
lst1=[123,4245,5422324,2323,133,533,543,622,1667]
lst1.sort()
print(lst1)
#降序
lst1.sort(reverse=True)
print(lst1)
#嵌套 lst[2][3][1]
#循环删除 *
#for i in lst:
 #   if i.startswith("王"):
 #       lst.remove(i)
 #DONOT WORK 索引乱了
for i in lst.copy():
    if i.startswith('王'):
        lst.remove(i)
print(lst)
