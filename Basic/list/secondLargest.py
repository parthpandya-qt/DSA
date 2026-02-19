def secondLargest(l):
    lar=l[0]
    slar=None
    for i in l:
        if(i>lar):
            
            slar=lar
            lar=i
        elif(i<lar):
            if(slar==None or slar<i):
                slar=i
    return slar          

l=[32,534,67,65,7,6,45,56,56,67,3]
print(secondLargest(l))





