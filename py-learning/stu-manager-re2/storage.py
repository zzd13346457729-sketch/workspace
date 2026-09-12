import json
#DATA="./data/re2.json"
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent##
DATA=BASE_DIR/"data"/"re2.json"##

def valid_students(data):
    if type(data) is not dict:
        return False
    for name,score in data.items():##
        if type(name) is not str or type(score) not in (int,float):
            return False##
        if not name.strip():
            return False
        if not (0<=score<=100):
            return False
    return True

def read_students():
    try:
        DATA.parent.mkdir(parents=True, exist_ok=True)##
        with open(DATA, "r", encoding="utf-8") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = {}
    except UnicodeDecodeError:#
        print("数据文件不是有效的UTF-8文本，请检查文件编码")
        return
    except OSError as e:##
        print(f"无法创建数据目录或读取文件：{e}")
        return
    except json.JSONDecodeError:
        print("数据文件不是有效JSON，请检查文件后重新运行")
        return
    if not valid_students(students):##
        print("文件中数据结构不合格，请检查文件后重新运行")
        return
    return students

def save_students(students):
    try:
        if not valid_students(students):##
            print("数据结构不合格，保存失败")
            return
        with open(DATA,"w",encoding="utf-8")as f:
            json.dump(students,f,ensure_ascii=False,indent=4)
    except OSError as e:
        print(f"{e}，保存失败")