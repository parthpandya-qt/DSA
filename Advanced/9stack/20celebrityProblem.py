def celebrity(mat):
    start = 0
    end = len(mat)-1
    while start<end:
        if mat[start][end] == 1:
            start += 1
        elif mat[end][start] == 1:
            end -= 1
        else:
            start+=1
            end-=1
    for i in range(len(mat)):
        if i == start:
            continue
        else:
            if mat[start][i] == 1 or mat[i][start] == 0:
                return -1
    return start








#implementation using the stack:
def celebrity(mat):

    n = len(mat)

    stack = []

    # Push all people
    for i in range(n):
        stack.append(i)

    # Eliminate candidates
    while len(stack) > 1:

        a = stack.pop()
        b = stack.pop()

        if mat[a][b] == 1:
            # a knows b
            stack.append(b)
        else:
            # a does not know b
            stack.append(a)

    candidate = stack.pop()

    # Verify candidate
    for i in range(n):

        if i == candidate:
            continue

        if mat[candidate][i] == 1:
            return -1

        if mat[i][candidate] == 0:
            return -1

    return candidate


mat = [
    [0, 1, 1],
    [0, 0, 0],
    [0, 1, 0]
]

print(celebrity(mat))