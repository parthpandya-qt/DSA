# def longestSubarray(arr):
#     n=len(arr)
#     res=0
#     for i in range(n):
#         count1=0
#         count0=0
#         for j in range(i,n):
#             if arr[j]==1:
#                 count1+=1
#             if arr[j]==0:
#                 count0+=1
#             if count0==count1:
#                 res=max(res,j-i+1)
#     return res

def longestSubarray(arr):
    n=len(arr)
    for i in range(n):
        if arr[i]==0:
            arr[i]=-1
    res=0
    Sum=0
    hashMap={}
    
    for i in range(n):
        Sum+=arr[i]
        if Sum==0:
            res=i+1
        elif Sum in hashMap:
            res=max(res,i-hashMap[Sum])
        else:
            hashMap[Sum]=i
    return res
            