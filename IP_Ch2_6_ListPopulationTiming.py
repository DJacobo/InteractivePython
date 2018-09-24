# Operation	Big-O Efficiency
# index []	        O(1)
# index assignment	O(1)
# append	        O(1)
# pop()	            O(1)
# pop(i)	        O(n)
# insert(i,item)	O(n)
# del operator	    O(n)
# iteration	        O(n)
# contains (in)	    O(n)
# get slice [x:y]	O(k)
# del slice	        O(n)
# set slice	        O(n+k)
# reverse	        O(n)
# concatenate	    O(k)
# sort	            O(n log n)
# multiply	        O(nk)

import timeit

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

# Testing different ways of initializing a list to a certain range of values
# t1 = timeit.Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000), "milliseconds")
# t2 = timeit.Timer("test2()", "from __main__ import test2")
# print("append ",t2.timeit(number=1000), "milliseconds")
# t3 = timeit.Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000), "milliseconds")
# t4 = timeit.Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000), "milliseconds")


# Testing efficiency of List popping, comparing popping end vs beginning at different sizes
popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

print("pop(0)   pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))
