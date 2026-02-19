def nextGreater(arr):
    stack=[]
    
    n=len(arr)
    res=[None]*n
    for i in range(n-1,-1,-1):
        while len(stack)>0 and stack[-1]<=arr[i]:
            stack.pop()
        if len(stack)==0:
            res[i]=-1
        else:
            res[i]=stack[-1]
        stack.append(arr[i])
    return res
        
            





arr = [4, 5, 2, 25]
print(nextGreater(arr))
