def palimdrom(n,start,end):
    if(start>=end):
        return True
    else:
        return (n[start]==n[end] and palimdrom(n,start+1,end-1))
