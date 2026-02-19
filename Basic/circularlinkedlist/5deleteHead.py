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
    print()

# def deleteHead(head):
#     if head==None:
#         return None
#     else:
#         curr=head
#         while curr.next!=head:
#             curr=curr.next
#         curr.next=head.next
#         return head.next
def deleteHead(head):
    if head==None:
        return None
    if head.next==None:
        return None
    else:
        head.key=head.next.key
        head.next=head.next.next
        return head


         

head=deleteHead(head)
head=deleteHead(head)
head=deleteHead(head)
traversal(head)