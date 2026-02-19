class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.sz=0

    def push(self,x):
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.sz+=1
    def pop(self):
        if self.head==None:
            return "Underflow"
        else:
            res=self.head.data
            self.head=self.head.next
            self.sz-=1
            return res
    def peek(self):
        if self.head==None:
            return "Underflow"
        else:
            return self.head.data
    def sizeOfstack(self):
        return self.sz
    def isEmpty(self):
        if self.head==None:
            return True
        return False
    
s=Stack()
s.push(10)    
s.push(20)    
s.push(30)

print(s.peek())

s.pop()

print(s.peek())

print(s.sizeOfstack())
