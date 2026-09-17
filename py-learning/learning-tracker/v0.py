from storage import load_records
from storage import save_records

def input_record():
    record={}
    record["subject"]=input("请输入学科：").strip()
    if not record["subject"]:
        print("输入不能为空，请重试")
        return None#
    while True:
        record["minutes"]=input("请输入时间(min)：").strip()
        if not record["minutes"]:
            print("输入不能为空/0，请重试")
            continue
        try:
            record["minutes"]=int(record["minutes"])
        except ValueError:
            print("数据类型错误，请输入整数")
            continue
        if record["minutes"] <= 0:#
            print("学习时间必须大于 0，请重试")
            continue
        break#
    record["content"]=input("请输入内容").strip()
    if not record["content"]:
            print("输入不能为空，请重试")
            return None#
    return record##

def print_records(records):
     for i in records:
          print(i)

def showcase_subject_time(records):
    total_dic={}
    for i in records:
          total_dic[i["subject"]]=total_dic.get(i["subject"],0)+i["minutes"]
            ####超级重要！
    return total_dic

def main():
    #record={}
    records=load_records()
    if records is None:
        print("读取失败，请检查数据文件")
        return
    total=0
    for record in records:
        total += record["minutes"]
    ysys=0
        #record={}
    while True:
            ys=input("是否进入记录？请输入yes or no").strip().lower()
            #if not ys=="yes" or ys=="no":
            if ys!="yes" and ys!="no":
                print("输入错误，请重试")
                continue
            else:
                break
    if ys=="yes":
         ysys+=1
    while ysys:
        record=input_record()
        if record is None:
             continue
        new_records = records + [record]
        if not save_records(new_records):
            print("本条记录未保存，本次录入结束")
            break
        records = new_records
        total += record["minutes"]
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
    print(f"总学习时间：{total}min")
    total_dic=showcase_subject_time(records)
    print(f"按科目分类：")
    for subject, minutes in total_dic.items():
        print(f"{subject}：{minutes} 分钟")
    ysys=0

if __name__ == "__main__":
    main()