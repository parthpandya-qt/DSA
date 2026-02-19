def maxKconsecutive(arr,k):
    n=len(arr)-k+1
    Max=float('-inf')
    for i in range(n):
        Sum=0
        for j in range(k):
            Sum+=arr[j+i]
        Max=max(Sum,Max)    
    return Max
print(maxKconsecutive([1, 2, 3, 4, 5], 2)) 
