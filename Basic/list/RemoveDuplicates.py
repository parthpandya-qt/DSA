def removeDuplicate(l):
    n=len(l)
    temp=[0]*n
    temp[0]=l[0]
    res=1
    for i in range(1,n):
        if temp[i-1]!=l[i]:
            temp[res]=l[i]
            res+=1
    for i in range(0,res):
        l[i]=temp[i]
    return res            

print(removeDuplicate([2,2,3,3,4,4,5,5,]))

def duplicate(l):
    n=len(l)
    res=1
    for i in range(1,n):
        if(l[res-1]!=l[i]):
            l[res]=l[i]
            res+=1
    return(res)    