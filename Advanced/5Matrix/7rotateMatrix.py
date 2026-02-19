def rotate90(mat):
    n=len(mat)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    for i in range(n):
        low=0
        high=n-1
        while low<high:
            mat[low],mat[high]=mat[high],mat[low]
            high-=1
            low+=1
            