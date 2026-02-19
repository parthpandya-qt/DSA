def stockSpan(arr):
    n=len(arr)
    for i in range(n):
        span=1
        j=i-1
        while j>=0 and arr[i]>=arr[j]:
            span+=1
            j-=1
        print(span, end=" ")
stockSpan([10,10,20,30,50,3,1,4,23])