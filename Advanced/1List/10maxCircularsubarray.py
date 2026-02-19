def maxCircular(arr,n):
    res=arr[0]
    for i in range(0,n):
        curr_sum=arr[i]
        curr_max=arr[i]
        for j in range(1,n):
            index=(i+j)%n
            curr_sum+=arr[index]
            curr_max=max(curr_sum,curr_max)
        res=max(res,curr_max)
    return res

def maxCircular(arr,n):
    res=0
    for i in range(n):
        for j in range(i+1,n):
            