def previousSmaller(arr):
    n = len(arr)
    ps = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        ps[i] = stack[-1] if stack else -1
        stack.append(i)

    return ps
def nextSmaller(arr):
    n = len(arr)
    ns = [n] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        ns[i] = stack[-1] if stack else n
        stack.append(i)

    return ns
def largestArea(arr):
    n = len(arr)
    ps = previousSmaller(arr)
    ns = nextSmaller(arr)

    maxArea = 0
    for i in range(n):
        width = ns[i] - ps[i] - 1
        area = arr[i] * width
        maxArea = max(maxArea, area)

    return maxArea
arr = [6, 2, 5, 4, 5, 1, 6]
print(largestArea(arr))
