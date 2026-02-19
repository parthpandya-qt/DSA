def subArraygivenSum(arr,Sum):
    curr=0
    s=0
    for i in range(len(arr)) :
        curr+=arr[i]
        while curr>Sum:
            curr-=arr[s]
            s+=1
        if curr==Sum:
            return True
    return False
 

      