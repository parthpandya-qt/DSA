
def exactlyThreeDivisors(n):
    if(n<2):
        return 0
    res = []
    def isPrime(num):
        for i in range(2,num):
            if(num%i==0):
                return False
        return True
    i=2
    while i*i<=n:
        if(isPrime(i)):
            res.append(i*i)
    return res





    