def mergeSubarray(a,low,mid,high):
    left = a[low:mid+1]
    right= a[mid+1:high+1]
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
            a[k]=left[i]
            k+=1
            i+=1
        else:
            a[k]=right[j]
            k+=1
            j+=1
    while i<len(left):
        a[k]=left[i]
        k+=1
        i+=1
    while j<len(right):
        a[k]=right[j]
        k+=1
        j+=1
    return a

     
def mergeSort(arr,l,r):
    if r>l:
        mid=(l+r)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        mergeSubarray(arr,l,mid,r)
                    

arr = [38, 27, 43, 3, 9, 82, 10]
mergeSort(arr, 0, len(arr) - 1)
print(arr)  
