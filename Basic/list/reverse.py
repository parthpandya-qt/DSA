def Reverse(l):
    res=len(l)-1

    
    ls=[]
    for i in range(0,len(l)):
        ls.append(l[res])
        res-=1
    return ls    
l=[1,2,3,4,5,6,7,8,9]
print(Reverse(l))


