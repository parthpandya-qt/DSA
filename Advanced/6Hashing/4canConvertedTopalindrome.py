def isPalindrome(str):
    hashMap={}
    for i in str:
        if i in hashMap:
            hashMap[i]+=1
        else:
            hashMap[i]=1
    odd=0
    for i in hashMap.values():
        if i%2!=0:
            odd+=1
    if odd>1:
        return False
    return True
