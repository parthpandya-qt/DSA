class Queue:
    def __init__(self,capacity):
        self.list=[None]*capacity
        self.cap=capacity
        self.size=0
        self.front=0
    def getFront(self):
        if self.size==0:
            return None
        else:
            return self.list[self.front]
    def getRear(self):
        if self.size==0:
            return None
        else:
            rear=(self.front+self.size-1)%self.cap 
            return self.list[rear]
    def enQueue(self,x):
        if self.size==self.cap:
            return 
        else:
            rear=(self.front+self.size-1)%self.cap 
            rear=(rear+1)%self.cap
            self.list[rear]=x
            self.size+=1
    def deque(self):
        if self.size==0:
            return None
        res=self.list[self.front]
        self.front=(self.front+1)%self.cap
        self.size-=1
        return res
        

q = Queue(5)
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
print(q.getFront())  # 10
print(q.getRear())   # 40
print(q.deque())     # 10
print(q.getFront())  # 20
q.enQueue(50)
print(q.getRear())   # 50
q.enQueue(60)        # Should fill the queue
print(q.getRear())   # 60
print(q.deque())     # 20
print(q.deque())     # 30
print(q.deque())     # 40
print(q.deque())     # 50
print(q.deque())     # 60
print(q.deque())     # None (queue is empty)