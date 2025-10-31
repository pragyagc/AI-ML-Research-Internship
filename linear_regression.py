import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


X=np.array([[1],[2],[3],[4],[5]])  #independent varaibale
y=np.array([2,4,5,4,5]) #dependent varaible

#creating model
model=LinearRegression()


#tarining the model
model.fit(X,y)


#predict
y_pred=model.predict(X)

#display results
print("Intercept:", model.intercept_)
print("Slope:", model.coef_)

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.show()