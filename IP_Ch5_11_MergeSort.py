# # Base: single item list is sorted
# # Split numList into halves
# # the halves will pass the leftmost index, and rightmost index

def mergeSortNoSlice(numList, leftPos, rightPos):
    if rightPos - leftPos == 1:
        return numList
    else:
        midpoint = (rightPos - leftPos) // 2
        return mergeRange(numList, leftPos, midpoint, rightPos)

# Start on the left of both lists, compare
# Take the smallest into the new list
# MERGE WITHOUT SLICES, RETURNS NEW LIST #TODO: Alternate version without new list
def mergeRange(numList, leftPos, midPoint, rightPos):
    leftIndex = leftPos
    leftEnd = midPoint
    rightIndex = midPoint
    rightEnd = rightPos
    mergeList = []
    # While comparing both, compare including rightEnd
    while leftIndex < leftEnd and rightIndex < rightEnd+1:
        if numList[leftIndex] <= numList[rightIndex]:
            mergeList.append(numList[leftIndex])
            leftIndex = leftIndex+1
        else:
            mergeList.append(numList[rightIndex])
            rightIndex = rightIndex+1
    while leftIndex < leftEnd:
        mergeList.append(numList[leftIndex])
        leftIndex = leftIndex+1
    while rightIndex < rightEnd+1:
        mergeList.append(numList[rightIndex])
        rightIndex = rightIndex+1
    return mergeList

# Base: single item list is sorted
# Split numList into halves
# the halves will pass the leftmost index, and rightmost index
def mergeSort(numList):
    if len(numList) <= 1:
        return numList
    else:
        midpoint = len(numList) // 2
        leftList = mergeSort(numList[0 : midpoint])
        rightList = mergeSort(numList[midpoint : len(numList)])
        return mergeLists(leftList, rightList)

# Start on the left of both lists, compare
# Take the smallest into the new list
def mergeLists(leftList, rightList):
    leftIndex = 0
    rightIndex = 0
    mergeList = []
    # While we can compare, do so
    while leftIndex < len(leftList) and rightIndex < len(rightList):
        if leftList[leftIndex] <= rightList[rightIndex]:
            mergeList.append(leftList[leftIndex])
            leftIndex = leftIndex+1
        else:
            mergeList.append(rightList[rightIndex])
            rightIndex = rightIndex+1
    # If right is entirely copied, but some left elements remain
    while leftIndex < len(leftList):
        mergeList.append(leftList[leftIndex])
        leftIndex = leftIndex+1
    while rightIndex < len(rightList):
        mergeList.append(rightList[rightIndex])
        rightIndex = rightIndex+1
    return mergeList


exList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(mergeSortNoSlice(exList, 0, len(exList)-1)) # TODO: Fix MergeSortNoSlice, it is broken
# print(mergeSort(exList))