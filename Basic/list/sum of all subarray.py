def print_subarrays(arr):
    n = len(arr)
    max=0
    for start in range(n):
        for end in range(start, n):
            sum=0
            for i in range(start, end + 1):
                sum+=arr[i]
            print(sum)
    


arr = [1, 2, 3]
print_subarrays(arr)