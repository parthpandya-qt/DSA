# def union(arr1,arr2):
#     n=len(arr1)
#     m=len(arr2)
#     res=[0]*(m+n)
#     for i in range(n):
#         res[i]=n[i]
#     for i in range(m):
#         res[n+1]=m[i]
#     ans=0
#     for i in range(len(res)):
#         temp=False
#         for j in range(i):
#             if res[i]==res[j]:
#                 temp=True
#                 break
#         if temp==False:
#             res+=1
#     return res
            
def union(arr1,arr2):
    us=set()
    for i in arr1:
        us.add(i)
    for i in arr2:
        us.add(i)
    return len(us)