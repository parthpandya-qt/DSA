from collections import deque

def Vertical(root):
    map = {}
    q = deque()
    level = deque()

    q.append(root)
    level.append(0)

    while q:
        curr_node = q.popleft()
        hd = level.popleft()

        if hd not in map:
            map[hd] = []

        map[hd].append(curr_node.data)

        if curr_node.left:
            q.append(curr_node.left)
            level.append(hd - 1)

        if curr_node.right:
            q.append(curr_node.right)
            level.append(hd + 1)

    for hd in sorted(map):
        for value in map[hd]:
            print(value, end=" ")

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


Vertical(root)






# from collections import deque

# def vertclalTraversal(root):
#     q = deque()
#     l = deque()
#     q.append(root)
#     l.append(0)
#     map = {}
#     res =[]
#     if root is None:
#         return {}
#     while q:
#         temp = q.popleft()
#         level = l.popleft()
#         if level not in map :
#             map[level] = []
#         map[level].append(temp.data)
#         if temp.left!=None:
#             q.append(temp.left)
#             l.append(level-1)
#         if temp.right!=None:
#             q.append(temp.right)
#             l.append(level+1)
#     sorted_dict = dict(sorted(map.items()))
#     for key,values in sorted_dict.items():
#         for j in values:
#             res.append(j)
#     return res


# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# print(vertclalTraversal(root))



