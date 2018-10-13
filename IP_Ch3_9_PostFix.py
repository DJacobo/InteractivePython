# The expression A + B * C. As shown above, A B C * + is the postfix equivalent
# The operands A, B, and C stay in their relative positions
# Only the operators change position

# Assume the infix expression is a string of tokens delimited by spaces.
# The operator tokens are *, /, +, and -, along with the left and right parentheses, ( and ).
# The operand tokens are the single-character identifiers A, B, C, and so on.
# The following steps will produce a string of tokens in postfix order.

# Create an empty stack called opstack for keeping operators. Create an empty list for output.
# Convert the input infix string to a list by using the string method split.
# Scan the token list from left to right.
# If the token is an operand, append it to the end of the output list.
# If the token is a left parenthesis, push it on the opstack.
# If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed.
#   Append each operator to the end of the output list.
# If the token is an operator, *, /, +, or -, push it on the opstack.
#   However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
# When the input expression has been completely processed, check the opstack.
#   Any operators still on the stack can be removed and appended to the end of the output list.

from pythonds.basic.stack import Stack
from IP_Ch3_6_BalanceParentheses import balanceString

def infixToPostfix(expression):
    if not balanceString(expression):
        raise SyntaxError('Parentheses are not balanced in the expression')
    precedence = {'**':4, '^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1 }
    # newExpression = expression.replace(' ', '')
    expList = expression.split(' ')
    opStack = Stack()
    output = []

    # for character in newExpression:
    for item in expList:
        if item in precedence:
            if item == '(':
                opStack.push(item)
            elif item == ')':
                poppedItem = opStack.pop()
                while poppedItem != '(':
                    output.append(poppedItem)
                    poppedItem = opStack.pop()
            else:
                while not opStack.isEmpty() and precedence.get(opStack.peek()) >= precedence.get(item):
                    output.append(opStack.pop())
                opStack.push(item)
        else:
            output.append(item)
    while not opStack.isEmpty():
        output.append(opStack.pop())
    return ' '.join(output)

# whenever an operator is seen on the input, the two most recent operands will be used in the evaluation
# Create an empty stack called operandStack.
# Convert the string to a list by using the string method split.
# Scan the token list from left to right.
#   If the token is an operand, convert it from a string to an integer and push the value onto the operandStack.
#   If the token is an operator, *, /, +, or -, it will need two operands. Pop the operandStack twice.
#       The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation.
#       Push the result back on the operandStack.
# When the input expression has been completely processed, the result is on the stack. Pop the operandStack and return the value.
def postfixEvaluation(postfix):
    # newPost = postfix.replace(' ', '')
    postList = postfix.split(' ')
    operators = '**^//+-()'
    operandStack = Stack()
    # for character in newPost:
    for item in postList:
        if item in operators:
            secondOp = operandStack.pop()
            firstOp = operandStack.pop()
            result = 0
            if item == '*':
                result = firstOp * secondOp
            elif item == '**' or item == '^':
                result = firstOp ** secondOp
            elif item == '/':
                result = firstOp / secondOp
            elif item == '+':
                result = firstOp + secondOp
            elif item == '-':
                result = firstOp - secondOp
            operandStack.push(result)
        else:
            operandStack.push(int(item))
    return operandStack.pop()


# process infix tokens from left to right and use two stacks, one for operators and one for operands
def infixEvaluation(expression):
    if not balanceString(expression):
        raise SyntaxError('Parentheses are not balanced in the expression')
    postList = expression.split(' ')
    precedence = {'**':4, '^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1 }

# PRAMP
# Given a string:
#     L is the letter,
#     N is the Newspaper
#     return True if L can be written entirely with N

def loveLetter(L, N):
    enoughLetters = True
    if len(L) > len(L):
        enoughLetters =  False
    else:
        lDict = {}
        # Get all required characters from the letter, and their counts
        for char in L:
            char = char.lower()
            if char == ' ':
                continue
            elif char in lDict:
                lDict[char] = lDict[char] + 1
            else:
                lDict[char] = 1
        
        # In the newspaper, decrement the count of the dictionary
        for char in N:
            char = char.lower()
            if char in lDict:
                lDict[char] = lDict[char] - 1
        
        # If the set has any positive values, there are not enough letters in the newspaper
        for key in lDict:
            if lDict[key] > 0:
                enoughLetters = False
        return enoughLetters

letter = 'Hello'
letter2 = ''
letter3 = 'iii'
news = 'In the beginning there was a lonely wolf'
news2 = 'ii ask dsak dsak'

print(loveLetter(letter, news))
print(loveLetter(letter, news2))

print(loveLetter(letter2, news))
print(loveLetter(letter2, news2))

print(loveLetter(letter3, news))
print(loveLetter(letter3, news2))
IslandCount