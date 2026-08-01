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
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count


def interSection(h1, h2):

    len1 = Count(h1)
    len2 = Count(h2)

    curr1 = h1
    curr2 = h2

    if len1 > len2:
        diff = len1 - len2
        for _ in range(diff):
            curr1 = curr1.next
    else:
        diff = len2 - len1
        for _ in range(diff):
            curr2 = curr2.next

    while curr1 is not None and curr2 is not None:
        if curr1 == curr2:
            return curr1.data

        curr1 = curr1.next
        curr2 = curr2.next

    return -1

