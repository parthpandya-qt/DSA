class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dequeue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.sz=0
    def size(self):
        if self.sz==0:
            return -1
        else:
            return self.sz
    def isEmpty(self):
        if self.sz==0:
            return True
        else:
            return False
    def insertRear(self,x):
        temp=Node(x)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
            temp.prev=self.rear
        self.rear=temp
        self.sz+=1
    def deleteFront(self):
        if self.front==None:
            return -1
        else:
            res=self.front.data
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            else:
                self.front.prev=None
            self.sz-=1
            return res

    def insertFront(self,x):
        temp=Node(x)
        if self.front==None:
            self.front=temp
        else:
            self.front.prev=temp
            temp.next=self.front
            self.front=temp
            temp.prev=None
        self.sz+=1    
    def deleteRear(self):
        if self.rear==None:
            return  -1
        res=self.rear.data
        self.rear=self.rear.prev
        if self.rear == None:
            self.front=None
        else:
            self.rear.next=None
        self.sz-=1
        return res        



dq = Dequeue()
print(dq.isEmpty())        # True
dq.insertRear(10)
dq.insertRear(20)
dq.insertFront(5)
dq.insertFront(1)
print(dq.size())           # 4
print(dq.deleteFront())    # 1
print(dq.deleteRear())     # 20
print(dq.deleteFront())    # 5
print(dq.deleteRear())     # 10
print(dq.deleteFront())    # -1 (empty)
print(dq.deleteRear())     # -1 (empty)
print(dq.size())           # 0
print(dq.isEmpty())        # True
            
        