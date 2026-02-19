class myHash:
    def __init__(self,c):

        self.cap=c
        self.table=[-1]*c
        self.size = 0
    def hash(self,x):
        return  x % self.cap
    def search(self,x):
        t=self.table
        h=self.hash(x)
        i=h
        while t[i]!=-1:
            if t[i] == x:
                return True
            i=(i+1)% self.cap
            if i==h:
                return False
        return False    
    def insert(self,x):
        if self.size==self.cap:
            return False
        if self.search(x)==True:
            return False
        i=self.hash(x)
        t=self.table
        while t[i] not in (-1,-2):
            i=(i+1)%self.cap
        t[i]=x
        self.size+=1
        return True
    def remove(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i] != -1:
            if(t[i]==x):
                t[i]=-2
                return True
            i=(i+1)%self.cap
            if i==h:
                return False
        return False    

h = myHash(7)
print(h.insert(10))  # True
print(h.insert(20))  # True
print(h.insert(15))  # True
print(h.insert(7))   # True
print(h.insert(22))  # True
print(h.table)       # Example: [22, 7, 15, -1, -1, 20, 10]

print(h.search(15))  # True
print(h.search(99))  # False

print(h.remove(15))  # True
print(h.table)       # 15 slot should be -2 now

print(h.insert(15))  # True (can re-insert after deletion)
print(h.table)


