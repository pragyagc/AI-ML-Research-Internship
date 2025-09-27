#1.list comprehension

#printing squares 
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  


#using with condition
evens = [n**2 for n in numbers if n % 2 == 0]
print(evens)


#using nested loop
pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)  





#2.dictionary comprehensions
nums = [1, 2, 3, 4]
squares_dict = {n: n**2 for n in nums}
print(squares_dict)   

#applying conditions
odd_squares = {n: n**2 for n in nums if n % 2 == 1}
print(odd_squares) 

#swapping  key and valyes of a dictionary
family_age = {"pragya": 21, "babin": 24, "pratyush": 15}
swapped = {v: k for k, v in family_age.items()}
print(swapped) 



#3. Set comprehensions
nums = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {n**2 for n in nums}
print(unique_squares)  

#cartesian products
a = {1, 2}
b = {3, 4}
pairs = {(x, y) for x in a for y in b}
print(pairs)  