# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
## Using String ONLY
# def isUnique(word):
#     pos = 0
#     stillOk = True
#     while pos < len(word) and stillOk:
#         substringList = word.split(word[pos])
#         if len(substringList) < 2:
#             pos = pos+1
#         else:
#             stillOk = False
#     return stillOk

# Using a list
def isUnique(word):
    wordList = list(word)
#     wordList = [character for character in word]
    wordList.sort()
    pos = 0
    stillOk = True
    while pos < len(wordList) and stillOk:
        if wordList[pos] not in wordList[pos+1:]:
            pos = pos+1
        else:
            stillOk = False
    return stillOk

# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Hints: #7, #84, #722, #737
def CheckPermutation(string1, string2):
    print('SKIPPED CUZ I ALREADY DID THIS')

def URLify(phrase):
    stripped = phrase.strip()
    url = stripped.replace(' ', '%20')
    return url