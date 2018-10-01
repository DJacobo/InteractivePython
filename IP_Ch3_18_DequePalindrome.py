from pythonds.basic.deque import Deque

# Make a deque, insert all characters from one end, then compare from both ends
def palindromeChecker(inString):
    isPalindrome = True
    characterDeque = Deque()
    for character in inString:
        characterDeque.addFront(character)
    
    while isPalindrome and characterDeque.size() > 1:
        if characterDeque.removeFront() != characterDeque.removeRear():
            isPalindrome = False
    return isPalindrome

print(palindromeChecker('radar'))
print(palindromeChecker('false'))