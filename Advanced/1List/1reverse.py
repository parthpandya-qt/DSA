def leftRotate(arr,d):
    n=len(arr)
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
def reverse(arr,l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

arr = [1, 2, 3, 4, 5]
d = 2

leftRotate(arr, d)
print(arr)
