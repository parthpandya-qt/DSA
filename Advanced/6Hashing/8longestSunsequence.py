# def longestSubsequence(arr):
#     arr.sort()
#     res=1
#     curr=1
#     n=len(arr)
#     for i in range(1,n):
#         if arr[i]==arr[i-1]:
#             continue
#         elif arr[i]==arr[i-1]+1:
#             curr+=1
#         else:
#             res=max(res,curr)
#             curr=1
#     return res
        
def longestSubsequence(arr):
    n=len(arr)
    Set=set()
    res=0
    for i in arr:
        Set.add(i)
    for i in arr:
        if (i-1) not in Set:
            curr=1
            while (i+curr) in Set:
                curr+=1
            res=max(res,curr)
    return res
