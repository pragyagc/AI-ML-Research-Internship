# Normal function
def square(x):
    return x * x

# Lambda equivalent
square_lambda = lambda x: x * x

print(square(5))         
print(square_lambda(5))  


#for adding two numbers
add=lambda a,b :a+b
print(add(2,3))




#using with map,filter and sorted

nums = [1, 2, 3, 4, 5]


doubled = list(map(lambda x: x * 2, nums))
print(doubled)  


# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens) 

# Sort tuples by second element
pairs = [(1, 5), (2, 2), (3, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
