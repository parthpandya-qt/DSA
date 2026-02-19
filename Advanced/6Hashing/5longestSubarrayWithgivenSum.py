def longestSubarray(arr,target):
    hashMap={}
    res=0
    prefixSum=0
    for i in range(len(arr)):
        prefixSum+=arr[i]
        if prefixSum==target:
            res=i+1
        elif prefixSum not in hashMap:
            hashMap[prefixSum]=i
        elif prefixSum-target in hashMap:
            res=max(res,i-hashMap[prefixSum-target])
    return res
