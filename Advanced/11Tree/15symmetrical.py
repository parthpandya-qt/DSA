def isSymmetrical(root):
    def check(left,right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        return (left.data == right.data and check(left.right,right.left) and check(left.left,right.right))
    return check(root.left,root.right)