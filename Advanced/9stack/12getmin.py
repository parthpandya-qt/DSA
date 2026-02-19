class stack:
    def __init__(self,cap):
        self.cap=cap
        self.arr=[None]*cap
        self.top=-1
        self.smaller=[None]*cap
        self.smallerTop=-1
    def push(self,x):
        if self.smallerTop==self.top==-1:
            self.top+=1
            self.smallerTop+=1
            self.arr[self.top]=x
            self.smaller[self.smallerTop]=x
        elif self.top<self.cap-1:
            if x > self.smaller[self.smallerTop]:
                self.top+=1
                self.arr[self.top]=x
            else:
                self.top+=1
                self.smallerTop+=1
                self.arr[self.top]=x
                self.smaller[self.smallerTop]=x
        else:
            print("overFlow")
    def pop(self):
        if self.top>-1:
            if self.arr[self.top]==self.smaller[self.smallerTop]:
                element=self.arr[self.top]
                self.top-=1
                self.smallerTop-=1
                return element
            else:
                element=self.arr[self.top]
                self.top-=1
                return element
        else:
            print("underflow")
    def getMin(self):
        if self.smallerTop == -1:
            return None
        return self.smaller[self.smallerTop]


    