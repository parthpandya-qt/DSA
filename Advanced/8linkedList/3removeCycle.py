def removeCycle(head):
    if head is None:
        return

    slow = head
    fast = head

    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    # No cycle
    if fast is None or fast.next is None:
        return

    # Find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Find last node of cycle
    while fast.next != slow:
        fast = fast.next

    # Remove cycle
    fast.next = None