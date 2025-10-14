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


#piechart
labels = ["Python", "C", "Java", "C++"]
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Programming Language Popularity")
plt.show()



#scatter plot
x = [5, 7, 8, 9, 10]
y = [10, 14, 15, 20, 25]

plt.scatter(x, y, color='orange')
plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()



#histogram
import numpy as np

data = np.random.randn(1000)  # 1000 random numbers
plt.hist(data, bins=20, color='purple')
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


#subplot(Multiple Graphs in One Figure)
x = [1, 2, 3, 4, 5]
y1 = [a**2 for a in x]
y2 = [a**3 for a in x]

plt.subplot(1, 2, 1)   # 1 row, 2 columns, plot 1
plt.plot(x, y1, 'r')
plt.title("Squares")

plt.subplot(1, 2, 2)   # plot 2
plt.plot(x, y2, 'g')
plt.title("Cubes")

plt.tight_layout()
plt.show()



#customizing graphs
plt.plot(x, y1, color='blue', linewidth=2, marker='s', markersize=6)
plt.title("Customized Plot", fontsize=14, color='darkred')
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.grid(True)
plt.show()








days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp = [30, 32, 31, 29, 35, 36, 34]

plt.plot(days, temp, color='orange', marker='o')
plt.title("Temperature Over a Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
