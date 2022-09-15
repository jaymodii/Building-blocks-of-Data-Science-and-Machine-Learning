import requests as r
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np
url=r.get("https://inshortsapi.vercel.app/news?category=sports")
d=url.json()
print("1).Number of main keys :",len(d))
print("The keys are :")
for i in d:
    print(i)
print("2).News available in this API :",len(d["data"]))
print("3).Here is the News :")
for i in range(0,len(d["data"])):
    print(i+1,".",d["data"][i]["content"],", Author :",d["data"][i]["author"],", DATE : ",d["data"][i]["date"])
print("--------------------------------------------------------------------------------------------------------------------")
url1=r.get("https://isro.vercel.app/api/spacecrafts")
d1=url1.json()
print("1).Number of main keys :",len(d1))
print("The keys are :")
for i in d1:
    print(i)
print("Total number of Spacecrafts are :",len(d1["spacecrafts"]))
print("2).List of Spacecrafts:")
for i in range(0,len(d1["spacecrafts"])):
    print(i+1," : ",d1["spacecrafts"][i]["name"])
in_name=input("3).Enter name of Spacecraft : ")
for i in range(0,len(d1["spacecrafts"])):
    if in_name==d1["spacecrafts"][i]["name"]:
        print("Spacecraft found")
        print( "-----------------------------------------------------------------------------------------------------------------------")
        break
else:
    print("Spacecraft not found")
    print("-----------------------------------------------------------------------------------------------------------------------")

url2=r.get("https://isro.vercel.app/api/customer_satellites")
d2=url2.json()
print("Main keys are : ")
countries=[]
counts=[]
for i in d2:
    print(i)
for i in range(0,len(d2["customer_satellites"])):
    countries.append(d2["customer_satellites"][i]["country"])
# print(countries)
counts=Counter(countries)
cname=counts.keys()
cval=counts.values()
# print(len(cname))
# explode=(0.0,0.1,0.0,0.1,0.0,0.1)
# print(cname)
# print(cval)

explode=[]

for j in range(0,len(cval)-1,3):
    if len(explode)<=23:
        i=0.0
        explode.append(i)
    if len(explode) <= 23:
        i=i+0.1
        explode.append(i)
    if len(explode) <= 23:
        i = i+0.1
        explode.append(i)

print(len(explode))
def make_autopct(cval):
    def my_autopct(pct):
        total = sum(cval)
        val = int(round(pct*total/100.0))
        return '{p:.2f}% \n (value:{v:d})'.format(p=pct,v=val)
    return my_autopct
plt.pie(cval,labels=cname,labeldistance=1.1,rotatelabels=bool,autopct=make_autopct(cval),pctdistance=0.6,textprops={'fontsize': 4})
plt.show()