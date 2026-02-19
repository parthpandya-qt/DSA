class Queue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        if len(self.queue)==0:
            return True
        return False
    def size(self):
        if not self.isEmpty():
            return len(self.queue)
    def enqueue(self,data):
        
        self.queue.append(data)
         
    def dequeue(self):
        if not self.isEmpty():
            item=self.queue[0]
            self.queue.pop(0)
            return item
        else:
            print("Underflow")
    def getFront(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            print("Empty queue") 
    def getRear(self):
        if not self.isEmpty():
            return self.queue[-1]
        else:
            print("Empty queue")

q = Queue()
print(q.isEmpty())      # True
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())         # 3
print(q.getFront())     # 10
print(q.getRear())      # 30
print(q.dequeue())      # 10
print(q.getFront())     # 20
print(q.size())         # 2
print(q.isEmpty())      # False
q.dequeue()
q.dequeue()
print(q.isEmpty())      # True
print(q.dequeue())      # Underflow