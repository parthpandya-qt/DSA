def spiral(root):
    stack1=[]
    stack2=[]
    stack1.append(root)
    while stack1 or stack2:
        while stack1:
            curr=stack1.pop()
            print(curr.data, end=" ")
            if curr.left:
                stack2.append(curr.left)
            if curr.right:
                stack2.append(curr.right)
        while stack2:
            curr=stack2.pop()
            print(curr.data, end=" ")
            if curr.right:
                stack1.append(curr.right)
            if curr.left:
                stack1.append(curr.left)
        