def factorial(n):
    fact=1
    if n==0:
        fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def dictionaryRank(txt):
    count=[0]*256
    n=len(txt)
    fact=factorial(n)
    for i in txt:
        count[ord(i)]+=1
    for i in range(1,256):
        count[i]+=count[i-1]
    for i in range(n):
        fact//=(n-i)
        smaller=count[ord(txt[i])-1]
        rank+=fact*smaller
        for j in range(ord(txt[i]),256):
            count[j]-=1
    return rank