def noOfSubarray(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            print(arr[j],end=" ")
        print()

print(noOfSubarray([3,5,6,3,3]))