def merge(a,b):
    res=[]
    x=len(a)
    y=len(b)
    i=0
    j=0
    while i<x and j<y:
        if a[i]<=b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    while i<x :
        res.append(a[i])
        i+=1
    while j<y:
        res.append(b[j])
        j+=1
    return res

print(merge([2,3,4,5,45],[1,23,56]))               
