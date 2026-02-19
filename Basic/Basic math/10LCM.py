# def LCM(x,y):
#     lcm=1
#     for i in range(1,x*y+1):
#         if(i%x==0 and i%y==0):
#             lcm=i
#             break
#     return i        
# print(LCM(15,10)) 


# def LCM(x,y):
#     res=max(x,y)
#     while True:
#         if(res%x==0 and res%y==0):
#             return res
#         res=res+1
#     return res    

# print(LCM(15,10))

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x    
def LCM(x,y):
    return x*y/gcd(x,y)

print(LCM(150,10))