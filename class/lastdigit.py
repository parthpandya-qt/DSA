def lastDigit(n):
    return abs(n) % 10


def compoundInterest(principal, rate, time):
    return principal * (1 + rate / 100) ** time    

def squareRoot(n):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return n ** 0.5

import math
def circle_area(radius):
    return math.pi * radius ** 2


