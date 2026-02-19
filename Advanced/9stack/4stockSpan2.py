def stockSpan(arr):
    n=len(arr)
    stack=[]
    stack.append(0)
    print(1, end=" ")
    for i in range(1,n):
        while len(stack)>0 and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if len(stack)==0:
            span=i+1
        else:
            span=i-stack[-1]
            
        print(span,end=" ")
        stack.append(i)


            