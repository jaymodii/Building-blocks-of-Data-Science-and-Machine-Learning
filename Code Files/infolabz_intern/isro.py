import requests as r
url = r.get("https://isro.vercel.app/api/spacecrafts")
data = url.json()
cnt = 1
print(f"Total Number of main keys : {len(data)}")
for i in data:
    print(f"{cnt}. {i}")
    cnt=cnt+1
cnt = 1

for i in range(0,len(data['spacecrafts'])):
    print(f"{cnt}. {data['spacecrafts'][i]['name']}")
    cnt=cnt+1
print("\n")
ip = input("Enter name of Spacecraft: ")
cnt = 1
fnd = 0
for i in range(0,len(data['spacecrafts'])):
    if data['spacecrafts'][i]['name'] == ip:
        fnd=1
        break
    else:
        fnd = 0
    cnt=cnt+1
if fnd == 1:
    print("spacecraft found")
else:
    print("spacecraft does not found!")
