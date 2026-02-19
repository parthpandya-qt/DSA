class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printList(head):
    cur=head
    while cur != None :
        print(cur.key, end = '->')
        cur = cur.next
head=None
def insertEnd(head,value):
    temp=Node(value)
    if head is None:
        return temp
    curr=head
    while curr.next != None:
        curr = curr.next
    curr.next=temp
    return head

def deleteFirst(head):
    if head==None:
        return None
    else:
        return head.next


head=None
head=insertEnd(head,10)
head=insertEnd(head,20)
head=insertEnd(head,30)
head=insertEnd(head,40)
head=deleteFirst(head)
printList(head)
