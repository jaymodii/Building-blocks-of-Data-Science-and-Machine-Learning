import matplotlib.pyplot as plt import pandas as pd import numpy as np from sklearn import linear_model, preprocessing
Dataset = pd.read_csv"orders.csv")
x = Dataset.iloc[:, 1].values X - X[:, np.newaxis] Y = Dataset.iloc[:, 2].values
poly = preprocessing.PolynomialFeatures(degree=5) x_polya poly.fit_transform(X) linear = Linear model. Linear regression() linear.fit(x_poly, Y) pred - linear.predict(x_poly)
plt.scatter(X, Y, color='blue') plt.plot(X, pred, color='red') plt.title('Polynomial Regression) plt.xlabel('Temperature) plt.vlabel("Pressure) plt.show()
print("Predicted Amount for id=8 : {linear.predict(poly.fit_transform [8]])}") print (f"Predicted Amount for id 9 : {linear.predict(poly.fit_transform [91])")