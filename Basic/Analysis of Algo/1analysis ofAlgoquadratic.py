def fun(n):
    sum = 0
    for i in range (1,1+n):
        for j in range(1,1+i):
            sum+=1
    return sum        


print(fun(4))