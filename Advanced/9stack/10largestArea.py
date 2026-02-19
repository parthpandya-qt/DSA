def largestArea(arr):
    n=len(arr)
    maxArea=0
    stack=[]
    for i in range(n):
        while len(stack)>0 and arr[stack[-1]]>=arr[i]:
            height=arr[stack.pop()]
            if not stack :
                width=i
            else:
                width=i-stack[-1]-1
            area=height*width
            maxArea=max(maxArea,area)
        stack.append(i)
    while stack:
        height=arr[stack.pop()]
        if not stack:
            width=n
        else:
            width=n-stack[-1]-1
        area=height*width
        maxArea=max(maxArea,area)
    return maxArea
        
            
