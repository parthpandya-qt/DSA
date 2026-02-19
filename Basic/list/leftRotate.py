def leftRotate(l):
    n=len(l)
    temp=[0]*n
    for i in range(0,n-1):
        temp[i]=l[i+1]
        temp[n - 1] = l[0]
    return temp

print(leftRotate([1,2,43,6,6]))    