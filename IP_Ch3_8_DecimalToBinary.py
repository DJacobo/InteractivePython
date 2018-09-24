# start with an integer greater than 0.
# A simple iteration then continually divides the decimal number by 2 and keeps track of the remainder
# The first division by 2 gives information as to whether the value is even or odd
# first remainder we compute will actually be the last digit in the sequence
from pythonds.basic.stack import Stack

def decimalToBinary(dec):
    binary = ''
    binaryStack = Stack()

    while dec > 0 or binaryStack.isEmpty():
        bit = dec % 2
        dec = dec // 2
        binaryStack.push(bit)
    while not binaryStack.isEmpty():
        binary = binary + str(binaryStack.pop())
    return binary

def baseToBinary(base, number):
    binary = ''
    remStack = Stack()

    while number > 0 or remStack.isEmpty():
        rem = number % base
        number = number // base
        remStack.push(rem)
    while not remStack.isEmpty():
        remCharacter = getCharacter(remStack.pop())
        binary = binary + remCharacter
    return binary

def getCharacter(index):
    characterString = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    character = characterString[index]
    return character

print('base: %s, num: %s, binary: %s' % (8, 25, baseToBinary(8, 25)))
print('base: %s, num: %s, binary: %s' % (16, 256, baseToBinary(16, 256)))
print('base: %s, num: %s, binary: %s' % (26, 26, baseToBinary(26, 26)))
# print('base: %s, num: %s, binary: %s' % (16, 10, baseToBinary(16, 10)))
# print('base: %s, num: %s, binary: %s' % (16, 10, baseToBinary(16, 10)))