def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n*factorial(n-1)
print(factorial(10))



def Sum(n):
    if n == 0:
        return 0
    return n+Sum(n-1)
print(Sum(100))