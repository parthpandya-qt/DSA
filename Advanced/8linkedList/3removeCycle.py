def removeCycle(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next
    if slow!=fast:
        return 
    slow=head
    while slow.next!=fast.next:
        slow=slow.next
        fast=fast.next
    fast.next=None
    