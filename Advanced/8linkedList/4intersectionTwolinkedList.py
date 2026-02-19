# def intersection(h1,h2):
#     s=set()
#     curr=h1
#     while curr!=None:
#         s.add(curr)
#         curr=curr.next
#     curr=h2
#     while curr!=None:
#         if curr in s:
#             return curr
#         curr=curr.next
def Count(head):
    count=0
    curr=head
    while curr!=None:
        count+=1
        curr=curr.next
    return count
def interSection(h1,h2):
    res1=Count(h1)
    res2=Count(h2)
    diff=abs(res1-res2)
    curr1=h1
    for _ in range(diff):
        if curr1==None:
            return -1
        curr1=curr1.next
    curr1=h1
    curr2=h2
    while curr1!=None and curr2!=None:
        if curr1==curr2:
            return curr1.data
        curr1=curr1.next
        curr2=curr2.next
    


