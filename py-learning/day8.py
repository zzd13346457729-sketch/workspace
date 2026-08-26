s="abcdefghijklmnopqrstuvwxyz"
print(len(s))
print(s[3:8:2])
s1=s.upper()
s=s.lower()
s=s.strip()
print(s,s1)

a="python_java_c++_ai"
b=a.replace("_","")
lst=a.split("_")
a1="-".join(lst)
print(a,b,a1,lst)

ret=s.find("1")
rec=s.find("b")
print(ret,rec)

dics={"zhang":80,"li":90}
print(dics.get("li"))