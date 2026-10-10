def pairSum(root,pairSum):
    hashMap = {}
    def check(node):
        nonlocal hashMap


        if node==None:
            return False
        if check(node.left):
            return True

        if pairSum-node.data in hashMap:
            return True
        hashMap[node.data] = True

        if check(node.right):
            return True
        return False
    return check(root)
