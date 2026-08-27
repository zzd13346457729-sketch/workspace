import json
with open("./data/test827.txt","w",encoding="utf-8") as f:
    f.write("我想要的想说的你全都知道\n")
    f.write("缓缓飘落的枫叶像思念\n")
    f.write("我不是天才\n")

with open("./data/test827.txt","a",encoding="utf-8") as f:
    f.write("想打好羽毛球，想创造出自己的意义\n") 

students={"zhang":89,"li":97}
with open("./data/827.json","w",encoding="utf-8") as f:
    json.dump(students,f,ensure_ascii=False,indent=4)
with open("./data/827.json","r",encoding="utf-8") as f:
    students2=json.load(f)
print(students2)