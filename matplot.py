import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


#for adding styles
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.title("Styled Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


#for drawing multiples line in one graph
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label="Squares")
plt.plot(x, y2, label="Linear", linestyle='--')
plt.legend()
plt.show()


#for bar chart
x = ["A", "B", "C", "D"]
y = [5, 7, 3, 8]

plt.bar(x, y, color='teal')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
