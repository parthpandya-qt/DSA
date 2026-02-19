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