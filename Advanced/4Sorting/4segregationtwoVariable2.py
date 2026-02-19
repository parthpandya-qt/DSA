def segregate(arr):
    i,j=-1,len(arr)
    while True:
        i+=1
        while i<len(arr) and arr[i]%2==0:
            i+=1
        j-=1
        while j>=0 and arr[j]%2!=0:
            j-=1
        if i>=j:
            return 
        arr[j],arr[i]=arr[i],arr[j]
        return arr
print(segregate([12,5,24,7,56,3,7]))