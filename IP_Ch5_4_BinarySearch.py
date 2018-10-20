def BinarySearch(searchList, searchItem):
    foundItem = False
    leftPos = 0
    rightPos = len(searchList)-1
    while not foundItem and leftPos <= rightPos:
        midPos = getMidPoint(leftPos, rightPos)
        if searchList[midPos] < searchItem:
            leftPos = midPos+1
        elif searchList[midPos] > searchItem:
            rightPos = midPos-1
        else: # searchList[midPos] == searchItem:
            foundItem = True
    return foundItem
    
def getMidPoint(leftPos, rightPos):
    return (leftPos + rightPos) // 2
