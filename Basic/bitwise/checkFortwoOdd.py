def checkTwoOdd(n):
    xor=0
    res1=0
    res2=0
    for i in n:
        xor=xor^i
    rb=xor&~(xor-1)
    for i in n:
        if (rb&i)!=0:
            res1=res1^i
        else:
            res2=res2^i
    return (res1,res2)

print(checkTwoOdd([13,13,13,45,45,56,56,3]))