try:
    num = int("abc") 
      # Error: cannot convert string to int
    result=10/0
except ValueError as e:
    print("Error:", e)
except ZeroDivisionError:
    print("Division by zero!")
finally: #usually used for cleaning or cloing files
    print("Done")


#for using else
try:
    x = int("5")
except ValueError:
    print("Error!")
else:
    print("Success:", x)




#raising exception

def check_age(age):
    if age <0:
     raise ValueError("age cant be nagtive")
    return age

print(check_age(21))
# check_age(-1)
try:
    check_age(-1)
except Exception as e:
    print("ERROR:",e)

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

print(withdraw(100, 50))   # 50
print(withdraw(500, 200))  # raises ValueError




#custom exception

class MyError(Exception):
    pass

try:
   raise MyError("Something went wrong!")
except MyError as e:
    print("Caught:", e) 





 #different arithmetic error
  
try:
    x = 10 / 0                # ZeroDivisionError
except ZeroDivisionError as e:
    print("Caught:", e)

try:
    y = int("abc")            # ValueError
except ValueError as e:
    print("Caught:", e)

try:
    z = "2" + 2               # TypeError
except TypeError as e:
    print("Caught:", e)


# LookupError family
try:
    my_list = [1, 2, 3]
    print(my_list[5])         # IndexError
except IndexError as e:
    print("Caught:", e)

try:
    my_dict = {"a": 1}
    #my_dict = {"a": 1,"b":2}
    print(my_dict["b"])       # KeyError
except KeyError as e:
    print("Caught:", e)


# File & OS Errors
try:
    f = open("nofile.txt")    # FileNotFoundError
except FileNotFoundError as e:
    print("Caught:", e)

import os
try:
    os.chdir("unknown_dir")   # NotADirectoryError / FileNotFoundError
except OSError as e:
    print("Caught:", e)


# Attribute & Name Errors
try:
    "hello".not_a_method()    # AttributeError
except AttributeError as e:
    print("Caught:", e)

# try:
#     print(undeclared_variable)     # NameError
# except NameError as e:
#     print("Caught:", e)


# Import Errors
# try:
#     import not_a_module       # ModuleNotFoundError
# except ModuleNotFoundError as e:
#     print("Caught:", e)


# Iterators
try:
    it = iter([1])
    next(it)
    next(it)                  # StopIteration
except StopIteration as e:
    print("Caught:", e)


# Runtime & Recursion
def recurse():
    return recurse()
try:
    recurse()                 # RecursionError
except RecursionError as e:
    print("Caught:", e)


# System-related
import sys
try:
    sys.exit(0)               # SystemExit
except SystemExit as e:
    print("Caught:", e)

try:
    raise KeyboardInterrupt   # KeyboardInterrupt (simulated here)
except KeyboardInterrupt as e:
    print("Caught:", e)
