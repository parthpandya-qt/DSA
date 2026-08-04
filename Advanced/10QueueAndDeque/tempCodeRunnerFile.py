def recursiveReverseQueue(q):
    if not q:
        return
    x=q.popleft()
    recursiveReverseQueue(q)
    q.append(x)

print(reverseQueue(queue([1,2,3,4,5])))  # Output: deque([5, 4, 3, 2, 1]   )