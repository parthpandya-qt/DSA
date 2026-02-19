class Dequeue:
    def __init__(self,c):
        self.arr=[None]*c
        self.capacity=c
        self.sz=0
        self.front=0
    def insertFront(self,x):
        if self.sz==self.capacity:
            return -1
        else:
            self.front=(self.front-1)%self.capacity
            self.arr[self.front]=x
        self.sz+=1
    def insertRear(self,x):
        if self.sz==self.capacity:
            return -1
        else:
            newrear=(self.front+self.sz-1)%self.capacity
            newrear=(newrear+1)%self.capacity
            self.arr[newrear]=x
        self.sz+=1
    def deleteFront(self):
        if self.sz==0:
            return -1
        else:
            res=self.arr[self.front]
            self.front=(self.front+1)%self.capacity
        self.sz-=1
        return res
    def deleteRear(self):
        if self.sz==0:
            return -1
        else:
            
            rear=(self.front+self.sz-1)%self.capacity
        self.sz-=1
        return self.arr[rear]    

dq = Dequeue(5)
dq.insertRear(10)
dq.insertRear(20)
dq.insertFront(5)
dq.insertFront(1)
print(dq.deleteFront())  # 1
print(dq.deleteRear())   # 20
dq.insertRear(30)
dq.insertFront(0)
print(dq.deleteFront())  # 0
print(dq.deleteRear())   # 30
print(dq.deleteFront())  # 5
print(dq.deleteRear())   # 10
print(dq.deleteFront())  # -1 (empty)
