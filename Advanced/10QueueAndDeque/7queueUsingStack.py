#User function Template for python3
class StackQueue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def push(self, B):
        
        n=len(self.s1)
        for i in range(n):
            self.s2.append(self.s1.pop())
        self.s1.append( B)
        p=len(self.s2)
        for i in range(p):
            self.s1.append(self.s2.pop())
        
        
    
        # code here
    
    def pop(self):
        if not self.s1:
            return -1
        else:
            return self.s1.pop()
            