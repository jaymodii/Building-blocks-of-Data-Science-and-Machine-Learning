

import requests as r
from matplotlib import pyplot as plt
own = r.get("https://isro.vercel.app/api/spacecrafts")
cust = r.get("https://isro.vercel.app/api/customer_satellites")
owndata = own.json()
custdata = cust.json()
total_spacecrafts = len(owndata['spacecrafts']) + len(custdata['customer_satellites'])
ownpercentage = round((len(owndata['spacecrafts'])*100)/(total_spacecrafts),2)
custpercentage = round((len(custdata['customer_satellites'])*100)/(total_spacecrafts),2)
percentages = [ownpercentage, custpercentage]
labels= [f"ISRO'S own spacecrafts({ownpercentage}%)",f"Customer Satellites ({custpercentage}%)"]
colors = ['#eb6e15','#8a84cc']
plt.pie(percentages, labels=labels, startangle=90, shadow=True, colors = colors)
plt.show()

