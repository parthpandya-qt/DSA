# def countset(n):
#     res=0
#     while n:
#         if (n%2==1):
#             res+=1
#         n=n//2
#     return res 

def countset(n):
    res=0
    while n:
        n=n&(n-1)
        res+=1
    return res    

print(countset(34))