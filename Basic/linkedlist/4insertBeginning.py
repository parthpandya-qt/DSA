class Node:
    def __init__(self,key):
        self.key=key
        self.next=None




head=None
def insertBegi(head,key):
    temp=Node(key)
    temp.next=head
    return temp
def printList(head):
    cur=head
    while cur != None :
        print(cur.key, end = '->')
        cur = cur.next

head=insertBegi(head,5)                 
 
head=insertBegi(head,10)                 

head=insertBegi(head,15)                 
printList(head)                   
