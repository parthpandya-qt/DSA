
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            mergedList = []
            for i in range(0,len(lists),2):
                first = lists[i]
                if i+1 < len(lists):
                    second = lists[i+1]
                else:
                    second = None
                mergedList.append(self.merge(first,second))
            lists = mergedList
        return lists[0]
    def merge(self,list1,list2):
        dummy = ListNode(-1)
        tail = dummy

        while list1 is not None and list2 is not None:

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
