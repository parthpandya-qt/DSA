def validate(root):
    def check(node, lower=None, upper=None):
        if node is None:
            return True

        if lower is not None and node.val <= lower:
            return False
        if upper is not None and node.val >= upper:
            return False

        return (
            check(node.left, lower, node.val)
            and check(node.right, node.val, upper)
        )

    return check(root)
