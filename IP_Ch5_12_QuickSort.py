def quickSort(numList):
    if len(numList) <= 1:
        return numList
    return partition(numList)

def partition(numList):
    pivot = medianOfThreeIndex(numList[0], 0, numList[len(numList)//2], len(numList)//2, numList[len(numList)-1], len(numList)-1)
    if pivot != 0:
        numList = swap(numList, 0, pivot)
    pivot = 0
    leftIndex = 1
    rightIndex = len(numList)-1
    while leftIndex <= rightIndex:
        while leftIndex <= rightIndex and numList[leftIndex] <= numList[pivot]:
            leftIndex = leftIndex+1
        while leftIndex <= rightIndex and numList[rightIndex] >= numList[pivot]:
            rightIndex = rightIndex-1
        if  leftIndex < rightIndex and numList[leftIndex] > numList[rightIndex]:
            numList = swap(numList, leftIndex, rightIndex)
    numList = swap(numList, pivot, rightIndex)
    return quickSort(numList[0:rightIndex]) + [numList[rightIndex]] + quickSort(numList[rightIndex+1:len(numList)])

def swap(numList, left, right):
    # swap, a,b = b,a
    numList[left], numList[right] = numList[right], numList[left]
    return numList

def medianOfThreeIndex(leftVal, left, midVal, mid, rightVal, right):
    medList = [leftVal, midVal, rightVal]
    medList.sort()
    if medList[1] == leftVal:
        return left
    elif medList[1] == midVal:
        return mid
    else:
        return right