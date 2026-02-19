def previousGreater(arr):
    n=len(arr)
    print(-1, end=" ")
    for i in range(1,n):
        j=i-1
        while j>=0 :
            if arr[j]>arr[i]:
                print(arr[j],end=" ")
                break
            j-=1
        else:
            print(-1, end=" ") 
