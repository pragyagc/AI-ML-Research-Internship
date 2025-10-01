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








#closure
def outer_function(msg):
    def inner_function():
        print("Message:", msg)  
    return inner_function

closure = outer_function("Hello Closure!")
closure()   


def multiplier(factor):
    def multiply_by(n):
        return n * factor
    return multiply_by

times2 = multiplier(2)
times3 = multiplier(3)

print(times2(5))
print(times3(5)) 





#recursion
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    return n * factorial(n - 1)

print(factorial(5)) 


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])  


