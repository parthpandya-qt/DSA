def segrgate(arr):
    i,j=-1,len(arr)
    while True:
        i+=1
        while i<len(arr) and  arr[i]<0:
            i+=1
        j-=1
        while j>=0 and arr[j]>=0:
            j-=1
        if i>=j:
            return arr
        arr[i],arr[j]=arr[j],arr[i]
    
