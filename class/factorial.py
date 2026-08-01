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

def natural(n):
    if n == 0:
        return 0 
    natural(n-1)
    print(n)
natural(10)

def palimdrom(n,start,end):
    if(start>=end):
        return True
    else:
        return (n[start]==n[end] and palimdrom(n,start+1,end-1))
