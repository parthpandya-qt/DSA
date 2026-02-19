# def HCF(x,y):
#     hcf=1
#     if(x>y):
#          limit=y
#     else:
#          limit=x
#     for i in range(1,limit+1):
#         if(x%i==0 and y%i==0):
#              hcf = i
#     return hcf 

# print(HCF(20,12))        

def HCF(x,y):
    
    while y:
        x,y=y,x%y
    return x 

print(HCF(10,10))
