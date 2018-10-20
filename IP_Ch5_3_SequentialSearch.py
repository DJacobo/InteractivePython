#               present:        NOT present
# Best Case     O(1)            O(n)
# Worst Case    O(n)            O(n)
# Average       O(n/2)          O(n)
def unorderedSequentialSearch(searchList, searchItem):
    foundItem = False
    pos = 0
    while not foundItem and pos < len(searchList):
        if searchItem == searchList[pos]:
            foundItem = True
        else:
            pos += 1
    return foundItem

#               present:        NOT present
# Best Case     O(1)            O(1)
# Worst Case    O(n)            O(n)
# Average       O(n/2)          O(n/2)
def orderedSequentialSearch(searchList, searchItem):
    foundItem = False
    pos = 0
    while not foundItem and pos < len(searchList):
        if searchItem == searchList[pos]:
            foundItem = True
        elif searchList[pos] > searchItem:
            break
        else:
            pos += 1
    return foundItem