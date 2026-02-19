def febonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return febonacci(n-1)+febonacci(n-2)

print(febonacci(10))        



def febonacci(n):
    arr=[]
    if n<=1:
        return n
    else:
        a,b=0,1
        arr.append(0)
        arr.append(1)

        for _ in range(2,n+1):
            a,b=b,a+b
            arr.append(b)
        return arr
print(febonacci(10))         