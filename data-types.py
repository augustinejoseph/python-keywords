# class
class Node:
    def __init__(self, data, Next=None):
        self.data = data
        self.next = next


node = Node(10)
print(node.data)


# def
def function(first, second):
    return first * second


res = function(2, 4)
print(res)

# del
del res, node
import math

del math

# global
global_10 = 10


def a_function():
    global global_10
    global_10 = 5
    print(id(global_10))
    return global_10


print(a_function())
print(global_10)
print(id(global_10))

# Lambda
result = lambda num: num * num
print(result)


# nonlocal
def my_func():
    number = 10
    print("outer id : ",id(number))
    print("outer", number)

    def inner_func():
        nonlocal number
        number = 5
        print("inner id : ",id(number))
        print("Inner", number)

    inner_func()
    print("outer id after running fn : ", id(number))
my_func()


# yield
def generator():
    for i in range(10):
        yield i

generator_obj = generator()
for num in generator_obj:
    print(num)