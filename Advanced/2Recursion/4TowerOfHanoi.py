def toh(n,a,b,c):
    if n==1:
        print("move 1 from",a,"to",c)
    else:
        toh(n-1,a,c,b)
        print("move",n,"from",a,"to",c)
        toh(n-1,b,a,c)

toh(4,"A","B","C")