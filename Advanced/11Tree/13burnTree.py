from collections import deque

def burnTree(root, leaf):

    
    parentMap = {}

    q1 = deque()
    q1.append(root)

    while q1:
        temp = q1.popleft()

        if temp.left:
            parentMap[temp.left.data] = temp
            q1.append(temp.left)

        if temp.right:
            parentMap[temp.right.data] = temp
            q1.append(temp.right)

   
    visitedMap = {}

    q2 = deque()
    q2.append(leaf)

    visitedMap[leaf.data] = 1

    time = 0

    while q2:

        size = len(q2)
        burned = False

        for _ in range(size):

            temp = q2.popleft()

           
            if temp.left and temp.left.data not in visitedMap:
                visitedMap[temp.left.data] = 1
                q2.append(temp.left)
                burned = True

      
            if temp.right and temp.right.data not in visitedMap:
                visitedMap[temp.right.data] = 1
                q2.append(temp.right)
                burned = True

            
            if temp.data in parentMap:

                parent = parentMap[temp.data]

                if parent.data not in visitedMap:
                    visitedMap[parent.data] = 1
                    q2.append(parent)
                    burned = True

        if burned:
            time += 1

    return time