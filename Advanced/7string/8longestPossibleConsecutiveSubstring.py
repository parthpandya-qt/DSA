def longest(txt):
    hashSet=set()
    n=len(txt)
    for i in range(n):
        hashSet.add(ord(txt[i]))
    ans=0
    for i in range(n):
        if ord(txt[i])-1 not in hashSet:
            res=0
            while res+ord(txt[i]) in hashSet:
                res+=1
            ans=max(ans,res)
    return ans
