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
def display(head):
    curr=head
    while curr!=None:
        print(curr.key,end="->")
        curr=curr.next


def delete_node(node):
    if node is None or node.next is None:
        raise Exception("Can't delete the last node or a None node this way.")
    
    next_node = node.next
    node.key = next_node.key
    node.next = next_node.next


delete_node(temp2)
display(head)        

