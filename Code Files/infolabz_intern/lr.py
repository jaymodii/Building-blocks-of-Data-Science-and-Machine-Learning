import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('C:\\Users\\JAY MODI\\PycharmProjects\\infolabz_intern\\prices.csv')
print(df)
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color="red")
plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
print(f"Predicted value of price: ",reg.predict([[int(input("Enter the value of area: "))]]))
#y=b0+b1x
print(f"Value of coefficient: ",reg.coef_)    # b1
print(f"value of intercept: ",reg.intercept_)  #bo
print("value of Y: ",reg.intercept_ + reg.coef_ * 3300)

