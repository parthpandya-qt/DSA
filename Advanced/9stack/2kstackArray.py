class kStack:
    def __init__(self,n,k):
        self.arr=[None]*n
        self.k=k
        self.n=n
        self.top=[-1]*k
        self.next=[i+1 for i in range(n)]
        self.next[n-1]=-1
        self.freeTop=0
    
    def push(self,sn,x):
        i=self.freeTop
        self.freeTop=self.next[i]
        self.arr[i]=x
        self.next[i]=self.top[i]
        self.top[sn]=i
    def pop(self,sn):
        i=self.top[sn]
        self.top[sn]=next[i]
        self.next[i]=self.freeTop
        self.freeTop=i
        return self.arr[i]
    def isEmpty(self,sn):
        if self.top[sn]==-1:
            return True



