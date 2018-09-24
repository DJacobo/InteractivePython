# operation	Big-O Efficiency
# copy	        O(n)
# get item	    O(1)
# set item	    O(1)
# delete item	O(1)
# contains (in)	O(1)
# iteration	    O(n)
import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
