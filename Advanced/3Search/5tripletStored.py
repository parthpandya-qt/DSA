def triplet(arr,x):
    n=len(arr)   
    for i in range(n-2):
        left=i+1
        right=n-1
        while left<right:
            if arr[left]+arr[i]+arr[right]==x:
                return True
            elif arr[left]+arr[right]+arr[i]>x:
                right-=1
            else:
                left+=1
    return False