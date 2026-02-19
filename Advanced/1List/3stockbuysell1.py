def maxProfit(arr,b,e):
    if e<=b:
        return 0
    res=0
    for i in range(b,e):
        for j in range(i+1,e):
            if arr[j]>arr[i]:
                curr=arr[j]-arr[i]+maxProfit(arr,b,i-1)+maxProfit(arr,j+1,e)
                res=max(res,curr)
    return res

print(maxProfit([1,5,3,1,2,8],0,5))