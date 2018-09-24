# check to see that each character in the first string actually occurs in the second. If it is possible to “checkoff” each character,
# then the two strings must be anagrams
# Checking off a character will be accomplished by replacing it with the special Python value None
# strings in Python are immutable, the first step in the process will be to convert the second string to a list
# Each character from the first string can be checked against the characters in the list and if found, checked off by replacement

# Analysis:
# Each of the n characters in s1 will cause iteration through n characters in s2
# Each of the n positions in the list will be visited to match with s1
# Number of visits becomes the sum of integers from 1 to n, simplifies to:
# (n(n+1))/2 = O(n^2)
def anagramCheckOff(s1, s2):
    stillOk = True
    lowerString = s1.lower()
    otherString = s2.lower()
    sList = list(otherString)

    if len(s1) != len(s2):
        stillOk = False

    if stillOk:
        for c in lowerString:
            if c in sList:
                pos = sList.index(c)
                sList[pos] = None
            else:
                stillOk =  False
                break
    return stillOk

# def bookAnagramCheckOff(s1, s2):
#     lowerString = s1.lower()
#     sList = list(s2.lower())

#     stillOk = True
#     pos = 0

#     while pos < len(lowerString) and stillOk:
#         pos2 = 0
#         found = False

#         while pos2 < len(sList) and not found:
#             if lowerString[pos] == sList[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1
        
#         if found:
#             sList[pos2] = None
#         else:
#             stillOk = False
        
#         pos = pos + 1
#     return stillOk

# ========================================================================================================================
# Another solution to the anagram problem will make use of the fact that even though s1 and s2 are different,
# they are anagrams only if they consist of exactly the same characters. So, if we begin by sorting each string alphabetically,
# from a to z, we will end up with the same string if the original two strings are anagrams

# Analysis:
# Each call to sort takes nlogn time, on both lists
# And the iteration through positions takes n time as well. Total time is:
# (nlogn) + nlogn + n = 2nlogn + n = O(nLog(n))
def anagramSortCompare(s1, s2):
    aList1 = list(s1.lower())
    aList2 = list(s2.lower())

    aList1.sort()
    aList2.sort()

    stillOk = True
    pos = 0

    if len(aList1) != len(aList2):
        stillOk = False

    while pos < len(aList1) and stillOk:
        if aList1[pos] == aList2[pos]:
            pos = pos+1
        else:
            stillOk = False

    return stillOk

# ========================================================================================================================
# Solution 3: Brute Force!
# simply generate a list of all possible strings using the characters from s1 and then see if s2 occurs
# there are n possible first characters, n−1 possible characters for the second position, n−2 for the third, and so on
# The total number of candidate strings is n∗(n−1)∗(n−2)∗...∗3∗2∗1, which is n!

# ========================================================================================================================
# Solution 4: count and compare
# count the number of times each character occurs
# Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character

# Analysis:
# Because none of our operations are nested, this should be a faster runtime
# We count the characters in each string (2n)
# And then compare both lists (26). Giving us a runtime of
# 2n + 26 = O(n)
def anagramCountCompare(s1, s2):
    lower1 = s1.lower()
    lower2 = s2.lower()

    count1 = [0]*26
    count2 = [0]*26

    stillOk = True
    if len(s1) == len(s2):
        for c in lower1:
            index = ord(c) - ord('a')
            count1[index] = count1[index] + 1
            
        for c in lower2:
            index = ord(c) - ord('a')
            count2[index] = count2[index] + 1
        
        j = 0
        while j < len(count1) and stillOk:
            if count1[j] == count2[j]:
                j = j+1
            else:
                stillOk = False
    else:
        stillOk = False
    return stillOk
