# Reduce the original number to a series of single-digit numbers.
# Convert the single digit-number to a string using a lookup.
# Concatenate the single-digit strings together to form the final result.

# ====================================================================== Book Differences
# Had the alphanumeric string outside of the if (really don't know why I put it in there)
# Instead of declaring numString, just returns the values directly

def numToBaseString(num, base):
    numString = ''
    if num < base:
        alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numString = alphanumeric[num]
    else:
        numString = numToBaseString(num // base, base) + numToBaseString(num % base, base)
    return numString

def recursiveReverseString(inString):
    if len(inString) <= 1:
        return inString
    else:
        return inString[-1] + recursiveReverseString(inString[:-1])

def palindromeDetector(inString):
    normalizedString = inString.lower().translate(str.maketrans('','', ' ,./<>?;\'’:[]{}\\|!@#$%^&*()_+-=)'))
    return normalizedString == recursiveReverseString(normalizedString)