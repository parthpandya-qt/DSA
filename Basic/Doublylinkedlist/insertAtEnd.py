class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def insertAtEnd(head,x):
    temp=Node(x)
    if head==None:
        return temp
    else:
        curr=head
        while curr.next!=None:
            curr=curr.next
        curr.next=temp
        temp.prev=curr
        return head    
    

head=None
head=insertAtEnd(head,10)
head=insertAtEnd(head,20)
head=insertAtEnd(head,30)

def traverse(head):
    curr=head
    while curr!=None:
        print(curr.data, end="->")
        curr=curr.next

traverse(head)