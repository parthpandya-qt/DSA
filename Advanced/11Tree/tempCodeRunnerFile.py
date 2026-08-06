from collections import deque

# def Vertical(root):
#     map={}
#     q=deque()
#     level=deque()
#     q.append(root)
#     level.append(0)
#     while q:
#         curr_node=q.popleft()
#         hd=level.popleft()
#         if hd not in map:
#             map[hd]=[]
#         map[hd].append(curr_node.data)
#         if curr_node.left:
#             q.append(curr_node.left)
#             level.append(hd-1)
#         if curr_node.right:
#             q.append(curr_node.right)
#             level.append(hd+1)
#     sorted_dict = dict(sorted(map.items(),  key=lambda x: x[0]))
#     for i in sorted_dict.values():
#         for j in i:
#             print(j ,end=" ")

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None