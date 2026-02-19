from collections import deque

def subarrayMAx(arr,k):
    q=deque()
    n=len(arr)
    for i in range(k):
        while q and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)
    print(arr[q[0]], end=' ')
    for i in range(k,n):
        while q and q[0]<=i-k:
            q.popleft()
        while q and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)
    print(arr[q[0]], end=' ')
        


        
