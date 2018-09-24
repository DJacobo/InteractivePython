# Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list. O(n2).
# The second function should be linear O(n).

import time
from random import randrange
def returnMinimumQuadratic(numList):
    minimum = numList[0]
    tempMin = numList[0]
    for i in numList:
        for j in numList:
            if i < j:
                tempMin = i
        if tempMin < minimum:
            minimum = tempMin
    return minimum

def returnMinimumLinear(numList):
    minimum = numList[0]
    for i in numList:
        if i < minimum:
            minimum = i
    return minimum

# testList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(returnMinimumQuadratic(testList))
# print(returnMinimumLinear(testList))

for listSize in range(1000, 10001, 1000):
    aList = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(returnMinimumQuadratic(aList))
    end = time.time()
    print('Quadratic! size: %s, time: %s' % (listSize, end-start))
    
    start = time.time()
    print(returnMinimumLinear(aList))
    end = time.time()
    print('Linear! size: %s, time: %s' % (listSize, end-start))
