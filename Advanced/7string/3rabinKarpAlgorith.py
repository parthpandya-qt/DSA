def rabinKarp(txt,pat,q):
    m,n=len(pat),len(txt)
    d=256
    h=1
    for _ in range(m-1):
        h=(h*d)%q
    
    p,t=0,0
    for i in range(m):
        p=(p*d+ord(pat[i]))%q
        t=(t*d+ord(txt[i]))%q
    for i in range(n-m+1):
        if p==t:
            for  j in range(m):
                if txt[i+j]!=pat[j]:
                    break
            else:
                print(i,end=" ")
        if i<(n-m):
            t=(d*(t-ord(txt[i])*h)+ord(txt[i+m]))%q
        if t<0:
            t=t+q
        

