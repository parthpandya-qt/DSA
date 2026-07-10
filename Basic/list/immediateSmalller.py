def immediateSmaller(n,x):
    smaller = float('-inf')
    for  i in range(len(n)):
        if n[i]<x and n[i]>smaller:
            smaller = n[i]
    return smaller

