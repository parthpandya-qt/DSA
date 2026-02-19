def minflip(arr,n):
    
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            if arr[i]!=arr[0]:
                print(f"from {i}")
            else:
                print(i-1)
    if arr[n-1]!=arr[0]:
        print(f"{n-1}")
        
            