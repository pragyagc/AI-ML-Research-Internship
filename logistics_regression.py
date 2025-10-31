#it is basicay classification algorithm
#we use sigmoid function  where it converts any real  number into probability between 0 and 1
import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5])
Y = np.array([0, 0, 0, 1, 1])

#initializing paaremeters
b0 = 0
b1 = 0
alpha = 0.1        # Learning rate
epochs = 1000       # Number of iterations

#sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for i in range(epochs):
    z = b0 + b1 * X
    Y_pred = sigmoid(z)
    
    # Compute gradients
    db0 = np.mean(Y_pred - Y)
    db1 = np.mean((Y_pred - Y) * X)
    
    # Update parameters
    b0 -= alpha * db0
    b1 -= alpha * db1

print(f"Intercept (b0): {b0:.3f}")
print(f"Coefficient (b1): {b1:.3f}")

# Predictions
z = b0 + b1 * X
Y_prob = sigmoid(z)
Y_pred_class = [1 if p >= 0.5 else 0 for p in Y_prob]

print("Predicted Probabilities:", Y_prob)
print("Predicted Classes:", Y_pred_class)

# Plot results
plt.scatter(X, Y, color='blue', label='Actual')
plt.plot(X, Y_prob, color='red', label='Sigmoid Curve')
plt.xlabel('X (Hours Studied)')
plt.ylabel('P(Y=1)')
plt.title('Logistic Regression from Scratch')
plt.legend()
plt.show()    



#using scikit-learn
from sklearn.linear_model import LogisticRegression
import numpy as np

# Data
X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([0, 0, 0, 1, 1])

# Model creation and training
model = LogisticRegression()
model.fit(X, Y)

# Predictions
Y_pred = model.predict(X)
Y_prob = model.predict_proba(X)

print("Predicted Probabilities:\n", Y_prob)
print("Predicted Classes:", Y_pred)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
