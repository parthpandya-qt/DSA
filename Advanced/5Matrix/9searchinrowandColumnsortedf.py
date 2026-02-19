def search(mat,x):
    r=len(mat)
    c=len(mat[0])
    i=0
    j=c-2
    while i<r and j>=0:
        if mat[i][j]==x:
            print (i,j , end=" ")
        elif mat[i][j]>x:
            j-=1
        else:
            i+=1
    print("not here") 
