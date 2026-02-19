# def divisior(n):
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i)

# divisior(7)

# def divisor(n):
#     x=1
#     while(x*x<=n):
#         if(n%x==0):
#             print(x) 
#             if(x!=n//x):
#                 print(n//x)
#         x=x+1            
              

# divisor(100)            
def divisor(n):
    i=1
    while(i*i<=n):
        if(n%i==0):
            print(i)
        i=i+1    
    i-=1
    while(i>=1):
        if(n%i==0):
            print(n/i)
        i-=1        
divisor(34)        

