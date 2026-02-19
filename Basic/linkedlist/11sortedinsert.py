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


def insertSorted(head,nodeToinsert):
    nodeToinsert=Node(nodeToinsert)
    if head==None:
        return nodeToinsert
    if nodeToinsert.key<head.key:
        nodeToinsert.next=head
        return nodeToinsert
    curr=head
    while curr.next!=None:
        if curr.next.key<nodeToinsert.key:
            curr = curr.next
        else:
            break
    nodeToinsert.next=curr.next
    curr.next=nodeToinsert
    return head        
    
        
def display(head):
    curr=head
    while curr!=None:
        print(curr.key,end="->")
        curr=curr.next
insertSorted(head,90)
insertSorted(head,25)
display(head)