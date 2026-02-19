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

def middleNode(head):
    if head==None:
        return None
    elif(head.next==None):
        return head
    else:
        count=0
        curr=head
        while curr!=None:
            curr=curr.next
            count+=1
        mid_index=count//2
        curr=head
        for i in range(mid_index):
            curr=curr.next
    print(curr.key)  



middleNode(head)
