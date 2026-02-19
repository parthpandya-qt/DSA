class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

head=Node(10)
temp2=Node(20)
temp3=Node(30)


head.next=temp2
temp2.prev=head

temp2.next=temp3
temp3.prev=temp2


