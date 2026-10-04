def identical(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 == None or root2 == None:
        return False

    if root1.data != root2.data:
        return False

    return identical(root1.left, root2.left) and \
            identical(root1.right, root2.right)







from collections import deque

def identical(root1, root2):
    q = deque([(root1, root2)])

    while q:
        n1, n2 = q.popleft()

        if n1 is None and n2 is None:
            continue

        if n1 is None or n2 is None:
            return False

        if n1.data != n2.data:
            return False

        q.append((n1.left, n2.left))
        q.append((n1.right, n2.right))

    return True