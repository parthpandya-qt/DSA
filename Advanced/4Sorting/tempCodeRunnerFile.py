def countingSort(arr,k):
    
    res=[0]*k
    output=[0]*len(arr)
    for i in arr:
        res[i]+=1
    for j in range(1,k):
        res[j]=res[j]-res[j-1]
    for x in range(len(arr)-1,-1,-1):
        output[res[x]-1]=x
        res[x]-=1
    for i in range(len(arr)):
        arr[i]=output[i]
    return arr
print(countingSort([5,4,2,5,6,4,2,1],7))