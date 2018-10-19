# ===================================================================================================== Book Explanation
# Create a recursive solution
#   A customer puts in a dollar bill and purchases an item for 37 cents. What is the smallest number of coins you can use to make change?
#   If we are trying to make change for the same amount as the value of one of our coins, the answer is easy, one coin
#       If we do not have a coin equal to the amount of change, we make recursive calls for each different coin value less than the amount of change we are trying to make
#       Adding 1 is the same as if we had made a recursive call asking where we satisfy the base case condition immediately
#   store the results for the minimum number of coins in a table when we find them.
# Memoization/Caching
#   Before we compute a new minimum, we first check the table to see if a result is already known
# 
# Truly Dynamic Process
# Our dynamic programming solution is going to start with making change for one cent and systematically work its way up to the amount of change we require
#     A penny plus the minimum number of coins to make change for 11−1=10 cents (1)
#     A nickel plus the minimum number of coins to make change for 11−5=6 cents (2)
#     A dime plus the minimum number of coins to make change for 11−10=1 cent (1)
# ====================================================================================================== My Solution
# Implement normal recursive solution first
# Added Memoization to improve performance
# Create a new method and use the dynamic programming methodology
#      Solved dynamically, by computing the minimum for 1, 2, 3,... onward recursively
# ======================================================================================================= differences
# The book passes in the coinList to each recursive call
#     Changed my solution to not have global list
# When checking for recursion they use a list comprehension
#     Changed my check inside the loop to comprehension as well
# Dynamic solution I created was still using recursion when there was really no need to
#     Changed to use a for loop to be more efficient
# The book uses the current value as the initial min, imitating that many pennies
#     Rarely will be the correct answer, but is a possibility instead of sys.maxsize
# The book stores the opimal coin at each value
#     Then another method goes backwards printing the coins to dispense them

import sys

def minCoins(changeDue, coinList):
    if changeDue <= 0:
        raise ValueError('Change Due must be a positive integer, greater than 0')
    knownValues = [0]*100
    return recurseCoins(changeDue, coinList, knownValues)

def recurseCoins(changeDue, coinList, knownValues):
    if changeDue in coinList:
        knownValues[changeDue] = 1
        return 1
    elif knownValues[changeDue] != 0:
        return knownValues[changeDue]
    else:
        realMin = sys.maxsize
        tempMin = sys.maxsize
        for coin in [c for c in coinList if c < changeDue]:
            coinMin = 1 + recurseCoins(changeDue-coin, coinList, knownValues)
            if coinMin < tempMin:
                tempMin = coinMin
        if tempMin < realMin:
            realMin = tempMin
        knownValues[changeDue] = realMin
        return realMin

def minCoinsDynamic(changeDue, coinList):
    if changeDue <= 0:
        raise ValueError('Change Due must be a positive integer, greater than 0')
    knownValues = [0]*100
    coinsUsed = [0]*100
    for value in range(1, changeDue+1):
        tempMin = value
        tempCoin = 0
        if value in coinList:
            knownValues[value] = 1
            coinsUsed[value] = value
        else:
            for previousCoin in [pc for pc in coinList if value-pc >= 0]:
                if knownValues[value-previousCoin] + 1 < tempMin:
                    tempMin = knownValues[value-previousCoin] + 1
                    tempCoin = previousCoin
            knownValues[value] = tempMin
            coinsUsed[value] = tempCoin
    # printCoins(coinsUsed, changeDue) # comment out for testing
    return knownValues[changeDue]

def printCoins(coinsUsed, changeDue):
    changeRemaining = changeDue
    while changeRemaining > 0:
        coin = coinsUsed[changeRemaining]
        print(coin)
        changeRemaining -= coin

# print(minCoins(99, [1, 5, 10, 21, 25, 50]))
# print(minCoinsDynamic(75, [1, 5, 10, 25]))
# print(minCoinsDynamic(33, [1, 5, 8, 10, 25]))