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

def reverse(head):
    if head==None:
        return None
    if head.next==None:
        return head
    curr=head
    new_head=None
    while curr!=None:
        new_head=curr
        curr.next,curr.prev=curr.prev,curr.next
        curr=curr.prev
    return new_head
head=reverse(head)    

def trverse(head):
    curr=head
    while curr!=None:
        print(curr.data,end="->")
        curr=curr.next

trverse(head)