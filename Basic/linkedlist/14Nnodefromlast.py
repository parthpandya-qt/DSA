class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

temp1=Node(10)
temp2=Node(20)
temp3=Node(30)
temp4=Node(40)

temp1.next=temp2
temp2.next=temp3
temp3.next=temp4


head=temp1
def display(head):
    curr=head
    while curr!=None:
        print(curr.key,end="->")
        curr=curr.next

def nodefromLast(head,n):
    if n==0:
        return head
    count=0
    curr=head
    while curr!=None:
        curr=curr.next
        count+=1
    index=count-n
    curr=head
    for _ in range(index):
        curr=curr.next
    print(curr.key)    

nodefromLast(head,3)