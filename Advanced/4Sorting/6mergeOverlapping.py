def mergeOverlapping(arr):
    arr.sort()
    n=len(arr)
    res=[]
    for i in arr:
        if not res or i[0]>res[-1][1]:
            res.append(i)
        else:
            res[-1][1]=max(res[-1][1],i[1])
    return res
       

       

