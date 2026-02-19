class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

head=Node(10)
temp2=Node(20)
temp3=Node(30)


head.next=temp2
temp2.prev=head

temp2.next=temp3
temp3.prev=temp2

def deleteTail(head):
    if head==None:
        return None
    if head.next==None:
        return None
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    
    return head    
        

def traverse(head):
    curr=head
    while curr!=None:
        print(curr.data, end="->")
        curr=curr.next


head=deleteTail(head)
head=deleteTail(head)

traverse(head)