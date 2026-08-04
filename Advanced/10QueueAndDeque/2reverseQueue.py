from collections import deque

def reverseQueue(q):
    stack = []

    while q:
        stack.append(q.popleft())

    while stack:
        q.append(stack.pop())


def recursiveReverseQueue(q):
    if not q:
        return

    x = q.popleft()
    recursiveReverseQueue(q)
    q.append(x)


q = deque([1, 2, 3, 4, 5])

reverseQueue(q)

recursiveReverseQueue(q)
print(q)