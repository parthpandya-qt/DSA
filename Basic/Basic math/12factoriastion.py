def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
        
        
def printPFactors(n):
    for i in range(2, n+1):
        if isPrime(i):
            
            while n % i == 0:
                print(i)
                n = n // i 

printPFactors(20)
        

def primefactor(x):
    if x==0 or x==1:
        return 0
    i=2
    while i*i<=x:
        while x%i==0:
            print(i)
            x//=i
        i+=1
    if x>1:
        print(x)