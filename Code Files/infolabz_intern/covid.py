import requests as r
url=r.get("https://data.covid19india.org/data.json")
d=url.json()
# print(d)
count=1
m = 0
for i in d:
    y = 1
    print("key :- ",count,":",i)
    for x in d['cases_time_series']:
        a = int(x['dailyconfirmed'])
        # print(a)
        print(f"{y,x}")
        if a>m:
           m=a
           max=d['cases_time_series'][y-1]['date']
        y+=1
    print("------------------------------------------------------------------")
    if(count==1):
        print(f"max number of cases = {m}")
        print(f"maximum cases on : {max}")
        print(f"Total number of keys :{y-1}")
    print("------------------------------------------------------------------")
    count+=1