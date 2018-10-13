# Most recent Opening ( must match the next closing )
# First opening ( may have to wait until the very last character for the closing )
# Implies a stack would be perfect

# Starting with an empty stack, process the parenthesis strings from left to right
# If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to appear later
# If, on the other hand, a symbol is a closing parenthesis, pop the stack
# If at any time there is no opening symbol on the stack to match a closing symbol, the string is not balanced properly
# At the end of the string, when all symbols have been processed, the stack should be empty
from pythonds.basic.stack import Stack

def balanceString(string):
    stack = Stack()
    isBalanced = True
    pos = 0
    while pos < len(string) and isBalanced:
        character = string[pos]
        if character in "([{":
            stack.push(character)
        # if character == '(' or character == '[' or character == '{':
        #     stack.push(character)
        elif character in ')]}':
        # elif character == ')' or character == ']' or character == '}':
            if stack.isEmpty():
                isBalanced = False
            elif not isMatch(stack.pop(), character):
                isBalanced = False
        pos = pos+1
    if isBalanced and stack.isEmpty():
        isBalanced = True
    else:
        isBalanced = False
    return isBalanced

def isMatch(openChar, closeChar):
    openChars = '([{'
    closeChars = ')]}'
    return openChars.index(openChar) == closeChars.index(closeChar)
    # match = True
    # if openChar == '(':
    #     if closeChar != ')':
    #         match = False
    # if openChar == '[':
    #     if closeChar != ']':
    #         match = False
    # if openChar == '{':
    #     if closeChar != '}':
    #         match = False
    # return match
