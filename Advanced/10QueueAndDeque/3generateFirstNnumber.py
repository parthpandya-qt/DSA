from collections import deque

def gernerate(n):
    
    q=deque()
    q.append('5')
    q.append('6')
    for i in range(n):
        curr=q.popleft()
        print(curr,end=' ')
        q.append(curr+'5')
        q.append(curr+'6')

