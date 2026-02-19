def radixSort(arr):
    mx=max(arr)
    exp=1
    while mx//exp>0:
        countingSort(arr,exp)
        exp*=10

def countingSort(arr,exp):
    ans=[0]*len(arr)
    res=[0]*10
    for i in range(0,len(arr)):
        index=(arr[i]//exp)%10
        res[index]+=1
    for i in range(1,len(res)):
        res[i]=res[i]+res[i-1]
    for i in range(len(arr)-1,-1,-1):
        index=(arr[i]//exp)%10
        ans[res[index]-1]=arr[i]
        res[index]-=1
    for i in range(len(arr)):
        arr[i]=ans[i]

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print(arr)
