from matplotlib import pyplot as plt
import requests as r
url=r.get("https://data.covid19india.org/data.json")
d=url.json()
states=[]
cases=[]
# print(d)
# states=d[1]["statecode"]
# print(states)
for i in range(1,len(d["statewise"])):
    states.append(d["statewise"][i]["state"])
    cases.append(d["statewise"][i]["confirmed"])

plt.barh(states,cases)
plt.show()