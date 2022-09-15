import requests as r
url=r.get("https://api.mfapi.in/mf")
d=url.json()
print(f"Total Records : ",len(d))
for i in range(0,len(d)):
    print(f"scheme code:{d[i]['schemeCode']}")


find=int(input ("Enter shceme code "))
flag=0
for i in range(0, len(d)) :
    if find == d[i]["schemeCode"] :
        flag=1
        print(d[i]["schemeName"])
        break
if flag==0:
    print("Can't find")
