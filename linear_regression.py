import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# X=np.array([[1],[2],[3],[4],[5]])  #independent varaibale
# y=np.array([2,4,5,4,5]) #dependent varaible

# #creating model
# model=LinearRegression()


# #tarining the model
# model.fit(X,y)


# #predict
# y_pred=model.predict(X)

# #display results
# print("Intercept:", model.intercept_)
# print("Slope:", model.coef_)

# # Plot
# plt.scatter(X, y, color='blue')
# plt.plot(X, y_pred, color='red')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Simple Linear Regression")
# plt.show()


#example for ordinart least squares:b1 = Σ((Xi - X̄)(Yi - Ȳ)) / Σ((Xi - X̄)²)  ;b0 = Ȳ - b1 * X̄
#model assumes  y'=b0+b1.X
# Sample data
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

# Step 1: Calculate means
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Step 2: Calculate coefficients
numerator = np.sum((X - mean_x) * (Y - mean_y))
denominator = np.sum((X - mean_x)**2)
b1 = numerator / denominator
b0 = mean_y - b1 * mean_x

print(f"Slope (b1): {b1:.3f}")
print(f"Intercept (b0): {b0:.3f}")

# Step 3: Predictions
Y_pred = b0 + b1 * X

# Step 4: Plot
plt.scatter(X, Y, color='blue', label='Actual')
plt.plot(X, Y_pred, color='red', label='Best Fit Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
