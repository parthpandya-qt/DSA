# def isPrime(n):
#     if(n==1):
#         return False
#     if(n==2 or n==3):
#         return True    
#     if(n%2==0 or n%3==0):
#         return False
#     i=5
#     while(i*i<=n):
#         if(n%i==0):
#             return  False
#         i=i+6
#     return True
    

# def SeiveOfEristhosis(n):
#     for i in range(2,1+n):
#         if isPrime(i):
#             print(i)


# SeiveOfEristhosis(20)

def sieve(n):
    if n==1:
        return
    isPrime=[True]*(n+1)
    i=2
    while i<=n:
        for j in range(i*i,n+1,i):
            isPrime[j]=False
        i+=1
    for i in range(2,n+1):
        if isPrime[i]:
            print(i)        

sieve(34)            