import timeit, random
# Devise an experiment to verify that the list index operator is O(1)
# for i in range(10000,1000001,20000):
#     t = timeit.Timer("x[random.randrange(%d)]"%i,
#                      "from __main__ import random,x")
#     x = list(range(i))
#     lst_time = t.timeit(number=1000)
#     print("%d,%10.3f" % (i, lst_time))
    
# Devise an experiment to verify that get item and set item are O(1) for dictionaries.

# Devise an experiment that compares the performance of the del operator on lists and dictionaries.

# # Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
# # def getKthSmallest(L, k):
#     # Could make a list that has K items, and moves across, replacing the current largest numbers by smaller ones as they are discovered
#     L.sort()
#     print(L)
#     return L[k-1]
# l = list(range(100))
# k = 10
# print(l)
# print('Get %sth smallest: %s' % (k, getKthSmallest(l, k)))

# Can you improve the algorithm from the previous problem to be linear? Explain.