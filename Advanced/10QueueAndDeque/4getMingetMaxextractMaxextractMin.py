from collections import deque


class solution:
    def __init__(self):
        self.q=deque()
    def insertMin(self,x):
        self.q.appendleft(x)
    def insertMax(self,x):
        self.q.append(x)
    def getMin(self):
        if len(self.q)!=0:
            return self.q[0]
    def getMax(self):
        if len(self.q)!=0:
            return self.q[-1]
    def extractMax(self):
        if len(self.q)!=0:
            curr=self.q.pop()
            return curr
    def extractMin(self):
        if len(self.q)!=0:
            curr=self.q.popleft()
            return curr 

