class Node:
    def __init__(self,k):
        self.key=k
        self.next=None


temp1=Node(10)
temp2=Node(20)
temp3=Node(30)
temp1.next=temp2
temp2.next=temp3
def printList(head):
    cur=head
    while cur != None :
        print(cur.key, end = '->')
        cur = cur.next
                   
head=temp1
def search(head,value):
    cur=head
    count=1
    while cur!=None:
        
        if cur.key==value:
            return count
        cur=cur.next
        count+=1
        
    return -1

print(search(head,10))