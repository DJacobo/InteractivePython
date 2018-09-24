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

def infixToPostfix(expression):
    precedence = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1 }
    newExpression = expression.replace(' ', '')
    opStack = Stack()
    output = []

    for character in newExpression:
        if character in precedence:
            if character == '(':
                opStack.push(character)
            elif character == ')':
                poppedChar = opStack.pop()
                while poppedChar != '(':
                    output.append(poppedChar)
                    poppedChar = opStack.pop()
            else:
                while not opStack.isEmpty() and precedence.get(opStack.peek()) >= precedence.get(character):
                    output.append(opStack.pop())
                opStack.push(character)
        else:
            output.append(character)
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
    newPost = postfix.replace(' ', '')
    operators = '*/+-()'
    operandStack = Stack()
    for character in newPost:
        if character in operators:
            secondOp = operandStack.pop()
            firstOp = operandStack.pop()
            result = 0
            if character == '*':
                result = firstOp * secondOp
            elif character == '/':
                result = firstOp / secondOp
            elif character == '+':
                result = firstOp + secondOp
            elif character == '-':
                result = firstOp - secondOp
            operandStack.push(result)
        else:
            operandStack.push(int(character))
    return operandStack.pop()

# postfixEvaluation('A B +')
print(postfixEvaluation('4 5 6 * +'))