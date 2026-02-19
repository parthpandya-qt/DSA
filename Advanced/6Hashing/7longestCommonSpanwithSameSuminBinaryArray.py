# def longest(arr1,arr2):
#     n=len(arr1)
#     res=0
#     for i in range(n):
#         sum1=0
#         sum2=0
#         for j in range(i,n):
#             sum1+=arr1[j]
#             sum2+=arr2[j]
#             if sum1==sum2:
#                 res=max(res,j-i+1)
#     return res
def longest(arr1, arr2):
    n = len(arr1)
    diff_map = {}
    max_len = 0
    pre_sum1 = pre_sum2 = 0
    for i in range(n):
        pre_sum1 += arr1[i]
        pre_sum2 += arr2[i]
        diff = pre_sum1 - pre_sum2
        if diff == 0:
            max_len = i + 1
        elif diff in diff_map:
            max_len = max(max_len, i - diff_map[diff])
        else:
            diff_map[diff] = i
    return max_len