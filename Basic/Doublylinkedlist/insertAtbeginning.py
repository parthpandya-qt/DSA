class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

head=None
def insertAtbegin(head,x):
    temp=Node(x)
    if head!=None:
        head.prev=temp
    temp.next=head
    return temp
head=insertAtbegin(head,10)
head=insertAtbegin(head,20)
head=insertAtbegin(head,30)

def traverse(head):
    curr=head
    while curr!=None:
        print(curr.data, end="->")
        curr=curr.next

traverse(head)

