import requests as r
url=r.get("https://inshortsapi.vercel.app/news?category=sports")
data=url.json()
cnt=1
print(f"Total number of main keys : {len(data)}")
for i in data:
    print(f"{cnt}. {i}")
    cnt+=1
print(f"Total News available : {len(data['data'])}\n")
cnt=1
for i in range(0,len(data['data'])):
    print(f"{cnt}. {data['data'][i]['content']}, Author: {data['data'][i]['author']}, DATE: {data['data'][i]['date']}")
    cnt+=1