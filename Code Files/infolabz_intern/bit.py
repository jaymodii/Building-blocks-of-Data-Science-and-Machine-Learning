import requests as r
url=r.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data=url.json()
print(data)
print("current bitcoin price :",data['bpi']['USD']['rate'],"dollars")
print(f"current bitcoin price : {data['bpi']['USD']['rate']}")