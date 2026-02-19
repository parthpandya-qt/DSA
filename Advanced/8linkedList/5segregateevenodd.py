def segregate(head):
    es,ee,os,oe=None,None,None,None
    curr=head
    while curr!=None:
        x=curr.data
        if x%2==0:
            if es==None:
                es=curr
                ee=es
            else:
                ee.next=curr
                ee=ee.next
        else:
            if os==None:
                os=curr
                oe=os
            else:
                oe.next=curr
                oe=oe.next
        curr=curr.next
    if os==None or es==None:
        return head
    ee.next=os
    oe.next=None
    return es 
