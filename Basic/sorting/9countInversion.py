# def inversion(l):
#     n=len(l)
#     count=0
#     for i in range(n-1):
#         for j in range(i+1,n):
#             if(l[i]>l[j]):
#                 count+=1
#     return count

# print(inversion([2,4,1,3,5]))
def inversion(arr,l,r):
    res=0
    if l<r:
        mid=(l+r)//2
        res+=inversion(arr,l,mid)
        res+=inversion(arr,mid+1,r)
        res+=countMerge(arr,l,mid,r)
    return res
def countMerge(arr,l,mid,r):
    left=arr[l:mid+1]
    right=arr[mid+1:r+1]
    i,j=0,0
    k=l
    res=0
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
            arr[k]=left[i]
            i+=1    
            k+=1
        elif(left[i]>right[j]):
            arr[k]=right[j]
            j+=1    
            k+=1        
            res+=len(left)-i
    while (i<len(left)):
        
        arr[k]=left[i]
        i+=1    
        k+=1
    while (j<len(right)):
        
        arr[k]=right[j]
        j+=1    
        k+=1        

