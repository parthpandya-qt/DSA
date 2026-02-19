class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None        
        self.rear=None
        self.sz=0
    def size(self):
        return self.sz
    def isEmpty(self):
        if self.sz==0:
            return True
        else:
            return False
    def enqueue(self,data):
        temp=Node(data)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.sz+=1
    def dequeue(self):
        if self.front==None:
            return None
        else:
            res=self.front.data
            self.front=self.front.next
            if self.front == None:
                self.rear=None
        self.sz-=1
        return res   

q = Queue()
print(q.isEmpty())      # True
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())         # 3
print(q.dequeue())      # 10
print(q.dequeue())      # 20
print(q.size())         # 1
print(q.isEmpty())      # False
print(q.dequeue())      # 30
print(q.isEmpty())      # True
print(q.dequeue())      # None 

                
