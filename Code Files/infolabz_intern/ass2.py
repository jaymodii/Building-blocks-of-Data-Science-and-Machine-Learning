import requests as r
url1=r.get("https://isro.vercel.app/api/spacecrafts")
d1=url1.json()
print("1).Number of main keys :",len(d1))
print("The keys are :")
for i in d1:
    print(i)