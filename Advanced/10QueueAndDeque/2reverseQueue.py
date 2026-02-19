from collections import queue

def reverseQueue(q):
    stack=[]
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
