from collections import deque
class Stack:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
    def push(self,data):
        self.q2.append(data)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1

    def pop(self):
        if self.q1:
            self.q1.popleft()
    def top(self):
        if self.q1:
            return self.q1[0]
        else:
            return None
    def size(self):
        if self.q1!=None:
            return len(self.q1)
        else:
            return None               
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.top())    # 30
print(s.pop())    # 30
print(s.top())    # 20
print(s.size())   # 2
print(s.pop())    # 20
print(s.pop())    # 10
print(s.pop()) 