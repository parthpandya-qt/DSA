from collections import deque


def firstCircularTour(petrol,distance):
    q=deque()
    n=len(petrol)
    if n<len(distance) or n>len(distance):
        return -1
    curr_petrol=0
    
    for start in range(2*n):
        idx=start%n
        q.append(idx)
        curr_petrol+=petrol[idx]-distance[idx]
        while curr_petrol<0 and q:
            x=q.popleft()
            curr_petrol-=petrol[x]-distance[x]
            
        if len(q)==n:
            return q[0]
    return -1    


            
