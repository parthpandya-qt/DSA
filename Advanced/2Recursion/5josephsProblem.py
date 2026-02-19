def jes(n,k):
    if n==1:
        return 0
    else:
        return (jes(n-1,k)+k)%n
    

print(jes(29,3))