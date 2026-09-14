def input_record():
    record={}
    record["subject"]=input("请输入学科：").strip()
    if not record["subject"]:
        print("输入不能为空，请重试")
        return
    record["minutes"]=input("请输入时间：").strip()
    if not record["minutes"]:
            print("输入不能为空/0，请重试")
            return
    while True:
        try:
            record["minutes"]=int(record["minutes"])
            break
        except ValueError:
            print("数据类型错误，请输入整数")
            continue
    record["content"]=input("请输入内容").strip()
    if not record["content"]:
            print("输入不能为空，请重试")
            return
    return record##

def print_records(records):
     for i in records:
          print(i)

def main():
    #record={}
    records=[]
    total=0
    while True:
        #record={}##
        record=input_record(record)
        total+=record["minutes"]
        records.append(record)
        while True:
            ys=input("是否退出记录？请输入yes or no").strip().lower()
            #if not ys=="yes" or ys=="no":
            if ys!="yes" and ys!="no":
                print("输入错误，请重试")
                continue
            else:
                 break
        if ys=="yes":
             break
        else:
             continue

    print_records(records)
    print(f"总学习时间：{total}")