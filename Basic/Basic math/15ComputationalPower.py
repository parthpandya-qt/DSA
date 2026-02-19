# def power(x,n):
#     res=1
#     for i in range (1,n+1):
#         res=res*x
#     return res    

# print(power(10,3))

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)

# print(power(2, 3))  # Output: 81
def Power(x):
    res = 1
    while n>0:
        if(n%2!=0):
            res=res*x
        x=x*x
        n=n//2
    return res        
