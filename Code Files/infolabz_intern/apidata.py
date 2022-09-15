import requests
url=requests.get("https://api.covidtracking.com/v2/states.json")
d=url.json()
print(d)