
def median(mat):
    r=len(mat)
    c=len(mat[0])
    mn,mx=0,mat[0][c-1]
    for i in range(1,r):
        mn=min(mn,mat[i][0])
        mx=max(mx,mat[i][c-1])
    tpos=(r*c+1)//2
    while mn<mx:
        mid=(mn+mx)//2
        midpos=0
        for i in range(r):
            midpos+=bisect_right(mat[i],mid)
        if midpos<tpos:
            mn=mid+1
        else:
            mx=mid
    return mn

def bisect_right(arr, x):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low

mat = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print(median(mat))