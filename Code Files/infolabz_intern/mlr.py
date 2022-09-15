import pandas as pd
from sklearn import linear_model

df = pd.read_csv('orderdata.csv')
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['users','orders','age']],df.amount)
print(f"Predicted amount is :",reg.predict([[int(input("Enter number of users: ")),int(input("enter number of orders: ")),int(input("Enter age : "))]]))