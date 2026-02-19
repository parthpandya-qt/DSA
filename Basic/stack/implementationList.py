class Stack:
    def __init__(self):
        self.stack=[]
    

    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return "Stack Underflow"
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return "Stack Underflow"
    def size(self):
        if not self.isEmpty():
            return len(self.stack)
        else:
            return "UnderFlow"
    
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.peek())
s.pop()
print(s.peek())
print(s.isEmpty())