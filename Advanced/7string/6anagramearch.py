def searchAnagram(txt,ana):
    n=len(txt)
    m=len(ana)
    ct=[0]*256
    ca=[0]*256
    res=[]
    for i in range(m):
        ct[ord(txt[i])]+=1
        ca[ord(ana[i])]+=1
    for i in range(n-m+1):
        if ct==ca:
            res.append(i) 
        if i+m<n:
            ct[ord(txt[i+m])]+=1
            ct[ord(txt[i])]-=1
    if res:
        return True
    else:
        return False