class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

temp1=Node(10)
temp2=Node(20)
temp3=Node(20)
temp4=Node(40)
temp5=Node(40)
temp6=Node(50)
temp7=Node(60)
temp8=Node(70)

temp1.next=temp2
temp2.next=temp3
temp3.next=temp4
temp4.next=temp5
temp5.next=temp6
temp6.next=temp7
temp7.next=temp8


head=temp1

def display(head):
    curr=head
    while curr!=None:
        print(curr.key,end="->")
        curr=curr.next


def reverse(head,prev=None):
    if head==None:
        return prev
    next=head.next
    head.next=prev
    return reverse(next,head)


display (reverse(temp1,None))   