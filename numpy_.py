import numpy as np


arr = np.array([1, 2, 3, 4, 5])  
print(arr)

mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat)
print(mat.ndim)   # Number of dimensions → 2
print(mat.shape)  # Shape (rows, columns) → (2, 3)
print(mat.size)   # Total elements → 6
print(mat.dtype)  # Data type → int64 (depends on system)


#creating specil array
np.zeros((2, 3))       # 2x3 matrix of 0s
np.ones((3, 2))        # 3x2 matrix of 1s
np.eye(3)              # 3x3 identity matrix
np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)   # 5 numbers between 0 and 1



#array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  
print(a * b)  
print(a ** 2) 


#mathematical function
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))     # 15
print(np.mean(arr))    # 3.0
print(np.max(arr))     # 5
print(np.min(arr))     # 1
print(np.std(arr))     # Standard deviation
print(np.sqrt(arr))    # [1. 1.41 1.73 2. 2.23]



#indexing and slicing

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])       
print(arr[-1])      
print(arr[1:4])   


mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[0, 1])     # 2
print(mat[:, 1])     # All rows, column 1 → [2 5 8]
print(mat[1, :])     # Row 1 → [4 5 6]
