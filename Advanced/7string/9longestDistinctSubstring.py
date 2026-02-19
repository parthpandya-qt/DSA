def longestDistinct(s):
    n=len(s)
    hashSet=set()
    maxLen=0
    l=0
    for r in range(n):
        while s[r] in hashSet:
            hashSet.remove(s[l])
            l+=1
        hashSet.add(s[r])
        maxLen=max(maxLen,r-l+1)
    return maxLen