class Node:
    def __init__(self, k):
        self.data = k
        self.next = None
        self.random = None

def clone(h1):
    if not h1:
        return -1
    curr=h1
    while curr:
        next1=curr.next
        curr.next=Node(curr.data)
        curr.next.next=next1
        curr=next1
    curr=h1
    while curr:
        if curr.random:
            curr.next.random=curr.random.next
        curr=curr.next.next
    curr=h1
    h2=h1.next
    clone=h2
    while curr:
        curr.next=curr.next.next
        if (clone.next==None):
            clone.next=None
        else:
            clone.next=clone.next.next
        clone=clone.next
        curr=curr.next
    return h2

