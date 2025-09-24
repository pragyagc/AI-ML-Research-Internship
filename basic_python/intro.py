print("Hello, Python!")  

#variables and bata type
age =20 #int
pi=3.14 #float
name = "Alice"  #string
is_student = True #bool

#operators
x = 10
y = 3
print(x + y)  
print(x ** y) #power
print(x > y and y < 5)  
# // this is wsed for floor division

#string
s = "Python"
print(s[0])   
print(s[1:4]) 
print(s.lower()) 
print(s.upper())


#control flow if else

x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


#fpr loop
for i in range(5):
    print(i) 

#while loop
i = 0
while i < 5:
    print(i)
    i+=1

#data structure

#list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])  


#tuple
colors = ("red", "green", "blue")
print(colors[1])  


#set
numbers = {1, 2, 3, 3}
print(numbers) 


#dictionary
person = {"name": "Alice", "age": 25}
print(person["name"])  
print(person["age"])  
person["age"] = 26
print(person["age"])

#function
def greet(name):
    return f"Hello, {name}!"

print(greet("Pragya")) 


#basic input output
name = input("Enter your name: ")
print("Hello", name)

print("running remaining codde")

#file read/write:
# Write to file
with open("file.txt", "w") as f:
    f.write("Hello Python\n")

# Read from file
with open("file.txt", "r") as f:
    print(f.read())


        
  

