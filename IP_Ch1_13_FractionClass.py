#  Example Class found here: 
#       http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
#  Create a class and override basic arithmetic operators
#      Use Euclid’s Algorithm for a helper function to assist in simplification of fractions -- gcd(m, n)
#          Euclid’s Algorithm states that the greatest common divisor of two integers m and n is n if n divides m evenly.
#          However, if n does not divide m evenly, then the answer is the greatest common divisor of n and the remainder of m divided by n
# -------------------TESTING-----------------------------------------
# cd "C:\Users\Daniel\Documents\Python Scripts\InteractivePython"
# pytest test_IP_Ch1_13_FractionClass.py
#--------------------------------------------------------------------

# Greatest Common Divisor: Number that is a common factor of both given numbers
def gcd(m, n):
    while(m % n != 0):
        oldM = m
        oldN = n

        m = oldN
        n = oldM % oldN
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.verifyInt(top, bottom)
        if bottom < 0:
            # convert both to ensure bottom is always positive
            bottom = abs(bottom)
            top = top * -1
        divisor = gcd(top, bottom)
        self.num = top//divisor
        self.den = bottom//divisor
    
    def __repr__(self):
        return 'Fraction(%r, %r) % (self.num, self.den)'

    def verifyInt(self, top, bottom):
        if not (isinstance(top, int) and isinstance(bottom, int)):
            raise TypeError('Require both top and bottom to be integers')

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, other):
        if isinstance(other, int):
            newNum = self.num + self.den*other
            newDen = self.den
        elif isinstance(other, Fraction):
            newNum = self.num*other.den + self.den*other.num
            newDen = self.den * other.den
        return Fraction(newNum, newDen) # divisor not necessary because reduced at init

    __radd__ = __add__ # 5.__add__(fraction) = fraction.__add__(5)
        
    # myF += yourF
    def __iadd__(self, otherFraction):
        newNum = self.num*otherFraction.den + self.den*otherFraction.num
        newDen = self.den * otherFraction.den
        return Fraction(newNum, newDen) # divisor not necessary because reduced at init
    
    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __sub__(self, otherFraction):
        newNum = self.num * otherFraction.den - self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        # divisor = gcd(newNum, newDen) 
        # return Fraction(newNum//divisor, newDen//divisor
        return Fraction(newNum, newDen)

    def __mul__(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        # divisor = gcd(newNum, newDen) 
        # return Fraction(newNum//divisor, newDen//divisor)
        return Fraction(newNum, newDen)

    def __truediv__(self, otherFraction):
        reciprocal = Fraction(otherFraction.den, otherFraction.num)
        newNum = self.num * reciprocal.num
        newDen = self.den * reciprocal.den
        # divisor = gcd(newNum, newDen)
        # return Fraction(newNum//divisor, newDen//divisor)
        return Fraction(newNum, newDen)

    # We can create deep equality - equality by the same value, not the same reference
    def __eq__(self, otherFraction):
        first = self.num * otherFraction.den
        second = self.den * otherFraction.num
        return first == second

    def __lt__(self, otherFraction):
        if self.den != otherFraction.den:
            newNum = self.num * otherFraction.den
            otherNum = self.den * otherFraction.num
            return newNum < otherNum
        else:
            return self.num < otherFraction.num
    
    def __le__(self, otherFraction):
        if self.den != otherFraction.den:
            newNum = self.num * otherFraction.den
            otherNum = self.den * otherFraction.num
            return newNum <= otherNum
        else:
            return self.num <= otherFraction.num

    def __gt__(self, otherFraction):
        if self.den != otherFraction.den:
            newNum = self.num * otherFraction.den
            otherNum = self.den * otherFraction.num
            return newNum > otherNum
        else:
            return self.num > otherFraction.num

    def __ge__(self, otherFraction):
        if self.den != otherFraction.den:
            newNum = self.num * otherFraction.den
            otherNum = self.den * otherFraction.num
            return newNum >= otherNum
        else:
            return self.num >= otherFraction.num

    def __ne__(self, otherFraction):
        first = self.num * otherFraction.den
        second = self.den * otherFraction.num
        return first != second

# newF = Fraction(2, 4)
# print(newF)
# print(newF.getNum())