class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


index = 0

inorder = [40, 20, 50, 10, 60, 30, 70]
preorder = [10, 20, 40, 50, 30, 60, 70]
end = len(inorder) - 1









def conversion(inorder,preorder,start,end):
    global index
    if end<start:
        return None
    root=Node(preorder[index])
    index+=1
    if start==end:
        return root
    for i in range(start,end+1):
        if (inorder[i]==root.data):
            break
    root.left=conversion(inorder,preorder,start,i-1)
    root.right=conversion(inorder,preorder,i+1,end)
    return root


def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.data] + inorderTraversal(root.right)


root = conversion(inorder, preorder, 0, end)
print(inorderTraversal(root))









def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = Node(preorder[0])

    mid = inorder.index(preorder[0])

    root.left = buildTree(
        preorder[1:mid + 1],
        inorder[:mid]
    )

    root.right = buildTree(
        preorder[mid + 1:],
        inorder[mid + 1:]
    )

    return root









def buildTree(self, preorder, inorder):
    self.pos = 0
    self.map = {value: i for i, value in enumerate(inorder)}

    def build(left, right):
        if left > right:
            return None

        root = Node(preorder[self.pos])
        self.pos += 1

        mid = self.map[root.val]

        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)

        return root

    return build(0, len(inorder) - 1)



