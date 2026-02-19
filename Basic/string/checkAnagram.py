def checkAnagram(x,y):
    if len(x)!=len(y):
        return False
    else:
        n=len(x)
        count=[0]*256
        for i in range(n):
            count[ord(x[i])]+=1
            count[ord(y[i])]-=1
        for x in count:

            if x!=0:
                return False
        return True         
            