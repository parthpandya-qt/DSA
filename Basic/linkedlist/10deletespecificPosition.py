class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

temp1=Node(10)
temp2=Node(20)
temp3=Node(30)
temp4=Node(40)
temp5=Node(50)
temp1.next=temp2
temp2.next=temp3
temp3.next=temp4
temp4.next=temp5

head=temp1
def display(head):
    curr=head
    while curr!=None:
        print(curr.key,end="->")
        curr=curr.next

def deleteSpecific(head,pos):
    if head is None:
        return None
    elif pos == 1:
        return head.next  # Remove head
    
    else:
        curr=head
        for i in range(pos-2):
            curr=curr.next
            if curr==None:
                return Node
        curr.next=curr.next.next    
    return Node

deleteSpecific(head,3)
display(head)