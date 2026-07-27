def fibonacci(n):
    if n == 1:
        print(1)
    elif n ==2:
        print(1,1)
    else:
        a=1
        b=1
        c=0
        print(a,b,end=" ")
        for i in range(n-2):
            
            c=a+b
            print(c,end=" ")
            a=b
            b=c
    
        

# fibonacci(10)


def fibonacci1(n):
    if n==0:
        return 1
    elif n ==1:
        return 2
    else:
        return fibonacci1(n-2)+fibonacci1(n-1)
print(fibonacci(10))