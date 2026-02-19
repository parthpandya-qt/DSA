class stack:
    def __init__(self,cap):
        self.cap=cap
        self.arr=[None]*cap
        self.top=-1
        self.min=-1
    def push(self,x):
        if self.top==-1:
            self.min=x
            self.top+=1
            self.arr[self.top]=x
        elif self.top>-1:
            if self.min>x:
                self.top+=1
                
                self.arr[self.top]=( x - self.min)
                self.min=x
            else:
                self.top+=1
                self.arr[self.top]=x 
        else:
            print("overflow")
    def pop(self):
        if self.top>-1:
            if self.arr[self.top]<=0:
                original = self.min
                x=self.arr[self.top]
                self.min = self.min - x  
                self.top-=1
                return original
            else:
                x=self.arr[self.top]
                self.top-=1
                return x
    def getMin(self):
        if self.top==-1:
            return None
        return self.min



