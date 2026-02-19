def snakePattern(temp):
    m=len(temp)
    n=len(temp[0])
    for i in range(m):
        if i%2==0:
            for j in range(n):
                print(temp[i][j])
        else:
            for j in range(n-1,-1,-1):
                print(temp[i][j])



arr=[[1,3,4,5,6],[7,5,34,2,67],[3,6,3,5,3]]
snakePattern(arr)