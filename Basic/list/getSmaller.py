def getSmaller(ls,n):
    newL=[]
    for i in ls:
        if(i<n):
            newL.append(i)
    return newL        
                 
ls=[3,4,6,45,34,22,1,]
n=15
print(getSmaller(ls,n))

