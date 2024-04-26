print('nice quantum')
def function(a,b):
    return 'b is greater than a' if a <b else 'a is greater than b'

print(function(5,4))
function = lambda a,b: 'b is greater than a' ,function(5,4) #another solution

# higher order functions

def cook(cool, a,b):
    return cool(a,b)

def func(a,b):
    return a * b

print(cook(func,5,6))

cook = lambda func,a,b: func(a,b)
func = lambda a,b: a*b

print(cook(func, 34,67))  #or

print((lambda func,a,b:func(a,b))(lambda a,b: a*b,6,7))


# GENERATORS IN PYTHON
#@ beginner level
def num_generator(n):
    for i in range(n):
        yield i

num_generat = (i for i in range(6))
for num in num_generat:
    print(num)
for num  in num_generator(5):  # using generator
    print(num)

# fibonancci
def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b = a, a+b # loop


fib_generator = fibo()
for _ in range(10):
    print(next(fib_generator))

nums = [2,3,4,5,6,7,8,9]
even = (num for num in nums if num % 2 == 0)
print(list(even))


#advanced generator

def read_large_files(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line

read_large_files = lambda file_path:(line for line in open(file_path,'r')) #or
#def read_large_files(file_path): return (line for line in open(file_path,'r'))


process_line = lambda line: print(line.strip().upper())

read_large = read_large_files('large.txt')
for line in read_large:
    process_line(line)


#example 2
def cyclic(elemnts):
    while True:
        yield from elemnts


cyclic_gen = cyclic(['a','b','c','d','e','f'])

for _ in range(10):
    print(next(cyclic_gen))


#Metaclasses from beginner to advanced

