def permutation(str,l,r):
    if r==l:
        print("".join(str))
    else:
        for i in range(l,r+1):
            str[i],str[l]=str[l],str[i]
            permutation(str,l+1,r)
            str[i],str[l]=str[l],str[i]

permutation(list("abc"),0,2)
            
