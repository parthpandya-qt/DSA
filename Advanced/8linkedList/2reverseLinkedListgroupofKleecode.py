def reverseGrou(head,k):
    curr=head
    prev_first=None
    first_pass=True
    while curr!=None:
        count=0
        temp=curr
        while temp!=None and count<k:
            temp=temp.next
            count+=1
        if count<k:
            if prev_first:
                prev_first.next=curr
            break
        first,prev=curr,None
        count=0
        while curr!=None and count<k:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count+=1
        if first_pass:
            head=prev
            first_pass=False
        else:
            prev_first.next=prev
        prev_first=first
    return head
