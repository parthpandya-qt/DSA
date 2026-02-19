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

def deleteHead(head):
    if head==None:
        return None
    if head.next==None:
        return None
    new_head=head.next
    new_head.prev=None
    head.next=None
    return new_head
        

def traverse(head):
    curr=head
    while curr!=None:
        print(curr.data, end="->")
        curr=curr.next


head=deleteHead(head)
head=deleteHead(head)

traverse(head)