# TODO: Everything
from IP_Ch3_8_DecimalToBinary import decimalToBinary
# 1) Convert the following values to binary using “divide by 2.” Show the stack of remainders.
#     17 -- 10001
#     45 -- 101101
#     96 -- 1100000
print('base: %s, num: %s, binary: %s' % (2, 17, decimalToBinary(17)))
print('base: %s, num: %s, binary: %s' % (2, 45, decimalToBinary(45)))
print('base: %s, num: %s, binary: %s' % (2, 96, decimalToBinary(96)))
# 2) Convert the following infix expressions to prefix (use full parentheses):
#     (A+B)*(C+D)*(E+F) --  * * + A B + C D + E F
#     A+((B+C)*(D+E)) -- + A * + B C + D E
#     A*B*C*D+E+F -- * C D + E F
# 3) Convert the above infix expressions to postfix (use full parentheses).
#     (A+B)*(C+D)*(E+F)
#     A+((B+C)*(D+E))
#     A*B*C*D+E+F
# 4) Convert the above infix expressions to postfix using the direct conversion algorithm.
#    Show the stack as the conversion takes place.
#     (A+B)*(C+D)*(E+F)
#     A+((B+C)*(D+E))
#     A*B*C*D+E+F
# 5) Evaluate the following postfix expressions. Show the stack as each operand and operator is processed.
#     2 3 * 4 +
#     1 2 + 3 + 4 + 5 +
#     1 2 3 4 5 * + * +
# 6) The alternative implementation of the Queue ADT is to use a list such that the rear of the queue is at the end of the list.
#    What would this mean for Big-O performance?
# 7) What is the result of carrying out both steps of the linked list add method in reverse order? What kind of reference results?
#    What types of problems may result?
# 8) Explain how the linked list remove method works when the item to be removed is in the last node.
# 9) Explain how the remove method works when the item is in the only node in the linked list.