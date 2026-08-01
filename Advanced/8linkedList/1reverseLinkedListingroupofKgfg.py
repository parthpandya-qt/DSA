def reverseGrou(head,k):
    curr=head
    prev_first=None
    first_pass=True
    while curr!=None:
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





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        dummyNode = ListNode(0,head)
        groupPrev = dummyNode
        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next
            prev,curr = kth.next,groupPrev.next
            while curr!=groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr=temp
            temp = groupPrev.next  
            groupPrev.next = kth
            groupPrev = temp
        return dummyNode.next



    def getKth(self,curr,k):
        while curr!=None and k>0:
            curr=curr.next
            k-=1
        return curr


    