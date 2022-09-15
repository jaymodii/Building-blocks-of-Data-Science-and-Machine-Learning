import requests as ro
from matplotlib import pyplot as plt
uk : rg.get("http://universities.hipolabs.com/search?country United Kingdom) US = rg.get("http://universities.hipolabs.com/search?country=United+States") ind = r.get("http://universities.hipolabs.com/search?country=india") pk = rg.get("http://universities.hipolabs.com/search?country=pakistan")
ukdata = uk.json() usdata = us.json inddata = ind.json pkdata = pk.json
countries = ["United Kingdom", "United States", "India", "Pakistan") universities = [len(ukdata), len(usdata), len(inddata), len(pkdata)]
plt. bar (countries, universities, color='maroon',
width_.-...0.5) plt.show()
country = input("Enter Country name : ") university = input("Enter University name :")

if country. Lower() = "united kingdom":
And = 0 for i in range(0, len(ukdata)): if ukdata ill'name').lower() = university.Lower();
print(f"University found. Visit {Ukdata[i]['web pages fnd = 1
break else:
fnd = 0 if fnd = 0:
print("Not found!")
elif country.lower() = "united states":
fnd = a for i in range(e, Len(usdata): if usdata is'name').lower = university.Lower
print("University found. Visit {usdata[i]['web pages' 110]}"), fnd = 1
break else:
fnd = 6 if fnd = 8:
print("Not found!")

elif country. Lower() = "india":
And = 8 for i in range(e, Len(inddata)): if inddata[i]['name' 1. lower() = university. lower(:
print("University found. Visit (inddata[i]['web_pages' []}") fnd = 1
break else:
fnd = @ if fnd = 0;
print("Not found!")
elif country.lower() = "pakistan":
fnd = 0 for i in range(e, Len(pkdata)): if pkdetail 'name').lower university. Lower();
print("University found. Visit {pkdata[i]['web pages [0] fnd = 1
break else:
fnd = 0 if fnd = B:
cint("Not found!")
else:
.print('Country Not Found! 2