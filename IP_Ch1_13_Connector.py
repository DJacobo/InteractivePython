# OOP design will use a connector between LogicGates
# Connector Has-A LogicGate

from IP_Ch1_13_LogicGate import *

class Connector:
    def __init__(self, fGate, tGate):
        self.fromGate = fGate
        self.toGate = tGate

        tGate.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate

# Given example
# g1 = AndGate("G1")
# g2 = AndGate("G2")
# g3 = OrGate("G3")
# g4 = NotGate("G4")
# c1 = Connector(g1,g3)
# c2 = Connector(g2,g3)
# c3 = Connector(g3,g4)
# print(g4.getOutput())

# # Self-Check - prove the following equality NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D)
# # NOT (( A and B) or (C and D))
# g1 = AndGate('A and B')
# g2 = AndGate('C and D')
# g3 = OrGate('g1 or g2')
# g4 = NotGate('NOT g3')
# c1 = Connector(g1,g3)
# c2 = Connector(g2,g3)
# c3 = Connector(g3,g4)
# print(g4.getOutput())

# # NOT( A and B ) and NOT (C and D)
# g1 = AndGate('A and B')
# g2 = AndGate('C and D')
# g3 = NotGate('NOT g1')
# g4 = NotGate('NOT g2')
# g5 = AndGate('g3 AND g4')
# c1 = Connector(g1,g3)
# c2 = Connector(g2,g4)
# c3 = Connector(g3,g5)
# c3 = Connector(g4,g5)
# print(g5.getOutput())

# Create a half-adder, which only adds two bits together:
#   2 inputs, A and B will generate two outputs, sum and carry
#       Sum = A XOR B, carry = A AND B
#       A,B = S,C   0,0 = 0,0   0,1 = 1,0   1,0 = 1,0   1,1 = 0,1
# g1 = XorGate('A XOR B')
# g2 = AndGate('A AND B')
# a = int(input('Please enter input for A'))
# b = int(input('Please enter input for B'))
# g1.pinA = a
# g1.pinB = b
# g2.pinA = a
# g2.pinB = b
# print('SUM = %s' % g1.getOutput())
# print('CARRY = %s ' % g2.getOutput())

# Create a full-adder, Uses 3 inputs, A B and Carry-in
# Results in a sum and carry out
# Create Circuit
x0 = XorGate('x0 - AB')
x1 = XorGate('x1 - Cinx0')
a0 = AndGate('a0 - Cinx0')
a1 = AndGate('a1 - AB')
o0 = OrGate('o0 - a0a1')
c0 = Connector(x0, x1)
c0 = Connector(x0, a0)
c0 = Connector(a0, o0)
c0 = Connector(a1, o0)
# Ask for inputs
a = int(input('Please enter input for A: '))
b = int(input('Please enter input for B: '))
cin = int(input('Please enter input for Cin: '))
#Set initial pins
x0.pinA = a
x0.pinB = b
x1.pinB = cin
a0.pinB = cin
a1.pinA = a
a1.pinB = b
#getOutput()
print('S = %s' % x1.getOutput())
print('Cout = %s' % o0.getOutput())

# HELL NO I'M NOT MAKING AN 8-BIT ADDER
# binaryAdd1 = [1, 0, 1, 0, 1, 0, 1, 0]
# binaryAdd2 = [0, 0, 1, 1, 0, 0, 1, 1]
# x0 = XorGate('x0')
# a0 = AndGate('a0')
# x1 = XorGate('x1')
# a1 = AndGate('a1')
# x2 = XorGate('x2')
# a2 = AndGate('a2')
# x3 = XorGate('x3')
# a3 = AndGate('a3')
# x4 = XorGate('x4')
# a4 = AndGate('a4')
# x5 = XorGate('x5')
# a5 = AndGate('a5')
# x6 = XorGate('x6')
# a6 = AndGate('a6')
# x7 = XorGate('x7')
# a7 = AndGate('a7')

# c0 = Connector()
# c1
