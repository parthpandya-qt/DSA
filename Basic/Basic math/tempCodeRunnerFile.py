
def countNegative(arr,k):
    j = 0
    n = len(arr)
    ans=[]
    for i in range(k,n):
        for k in range(j,i):
            if arr[k]<0:
                ans.append(arr[k])
            else:
                ans.append(arr[k])
        j+=1
    return ans

print(countNegative([-1,3,5,-3,-3,-5,5,23,-6],3))