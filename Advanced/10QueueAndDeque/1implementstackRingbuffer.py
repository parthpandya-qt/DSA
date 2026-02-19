class Deque:
    def __init__(self,cap):
        self.cap=cap
        self.front=0
        self.rear=0
        self.size=0
        self.arr=[None]*cap
    def getFront(self):
        if self.size==0:
            return None
        return self.arr[self.front]
    def getRear(self):
        if self.size==0:
            return None
        return self.arr[(self.front+self.size-1)%self.cap]
    def isEmpty(self):
        if self.size==0:
            return True
        else:
            return False
    def isFull(self):
        return self.size==self.cap
    def enqueue(self,x):
        if self.isFull():
            print("queue is full")
            return
        self.size+=1
        self.arr[self.rear]=x
        self.rear=(self.rear+1)%self.cap
    def dequeue(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            self.size-=1
            x=self.arr[self.front]
            self.front=(self.front+1)%self.cap
            return x


