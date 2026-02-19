def largestArea(arr):
    n=len(arr)
    res=0
    for i in range(n):
        curr=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>=arr[i]:
                curr+=arr[i]
            else:
                break
        for j in range(i+1,n):
            if arr[j]>=arr[i]:
                curr+=arr[i]
            else:
                break
        res=max(res,curr)
    return res


# naive Approach