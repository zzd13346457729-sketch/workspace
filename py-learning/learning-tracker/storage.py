import json
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent
DATA=BASE_DIR/"data"/"records.json"

def valid_data(data):
    if type(data) is not list:
        return False
    for record in data:
        if type(record) is not dict:
            return False
        subject = record.get("subject")
        minutes = record.get("minutes")
        content = record.get("content")

        if type(subject) is not str or not subject.strip():
            return False

        if type(minutes) is not int or minutes <= 0:
            return False

        if type(content) is not str or not content.strip():
            return False###
        #for k,v in record.items():
            ##return None
            #if type(v) not in (str,int):
            #    return None
            #if not k.strip():
            #    return None
            #if not v.strip():
            #    return None
            #if not (0<record["minutes"]):
            #    return None
    return True#
            

def load_records():
    try:
        DATA.parent.mkdir(parents=True,exist_ok=True)
        with open(DATA,"r",encoding="utf-8")as f:
            records=json.load(f)
    except FileNotFoundError:
        records=[]
    except UnicodeDecodeError:#
        print("数据文件不是有效的UTF-8文本，请检查文件编码")
        return
    except OSError as e:
        print(f"{e}，文件读取失败，请检查后重新运行")
        return
    except json.JSONDecodeError:
        print("文件中数据结构不合格，请检查文件后重新运行")
        return
    if not valid_data(records):##
            print("文件中数据结构不合格，请检查文件后重新运行")
            return None
    return records

def save_records(records):
    try:
        if not valid_data(records):##
            print("数据结构不合格，保存失败")
            return False
        DATA.parent.mkdir(parents=True, exist_ok=True)
        with open(DATA,"w",encoding="utf-8")as f:
            json.dump(records,f,ensure_ascii=False,indent=4)
    except OSError as e:
        print(f"{e}，保存失败")
        return False
    return True
    