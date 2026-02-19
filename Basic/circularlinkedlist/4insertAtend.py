class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
temp1=Node(10)        
temp2=Node(20)        
temp3=Node(30)        
temp4=Node(40)        
temp5=Node(50)        
temp6=Node(60)

head=temp1

temp1.next=temp2
temp2.next=temp3        
temp3.next=temp4        
temp4.next=temp5        
temp5.next=temp6        
temp6.next=head  

def traversal(head):
    if head==None:
        return None
    if head.next==None:
        return head
    curr=head
    while True:
        print(curr.key, end='->')
        curr=curr.next
        if curr==head:
            break
    

def insertAtEnd(head,data):
    temp=Node(data)
    if head==None:
        temp.next=temp
        return temp
    else:
        temp.next=head.next
        head.next=temp
        temp.key,head.key=head.key,temp.key
        return temp


head=insertAtEnd(head,23)
head=insertAtEnd(head,24)
head=insertAtEnd(head,25)
traversal(head)