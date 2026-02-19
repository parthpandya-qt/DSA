def previousGreater(arr):
    n=len(arr)
    stack=[]
    for i in range(n):
        while len(stack)>0 and stack[-1]<=arr[i]:
            stack.pop()
        if len(stack)==0:
            pg=-1
        else:
            pg=stack[-1]
        print(pg, end=" ")
        stack.append(arr[i])
    

arr = [10, 4, 2, 20, 40, 12, 30]
previousGreater(arr)
