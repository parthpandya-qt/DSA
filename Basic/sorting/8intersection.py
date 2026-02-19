def intersection(a,b):
    i=0
    j=0
    while i<len(a) and j<len(b):
        if(i>0 and a[i]==a[i-1]):
            i+=1
        elif(j>0 and b[j]==b[j-1]):
            j+=1  
        elif(a[i]==b[j]):
            print(a[i])
            i+=1
            j+=1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1    
