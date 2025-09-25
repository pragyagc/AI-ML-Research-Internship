a=33
b=200
if b> a:
    print("b is greater than a")


def display():
    for i in range(1,10):
        if i==10:
            print("done")
display()

#built in debugger:pdb
import pdb;
pdb.set_trace()

def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(5, 0))
