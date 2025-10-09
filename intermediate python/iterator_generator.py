#normal iteration
nums = [1, 2, 3]
for n in nums:
    print(n)


#manual iterator
nums=[1,2,3]
it=iter(nums)
print(next(it))
print(next(it))
print(next(it))
#if printed further ,it shows stopiteration error when there are no more items




#custom iterator
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in CountDown(5):
    print(num)




#generator
def count_down(start):
    while start > 0:
        yield start
        start -= 1

for num in count_down(5):
    print(num)



#using next manually
def gen_nums():
    yield 1
    yield 2
    yield 3

g = gen_nums()
print(next(g)) 
print(next(g))  
print(next(g))  
