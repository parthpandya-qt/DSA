# def secondLargest(l):
#     lar=l[0]
#     slar=None
#     for i in l:
#         if(i>lar):
            
#             slar=lar
#             lar=i
#         elif(i<lar):
#             if(slar==None or slar<i):
#                 slar=i
#     return slar  

def secondLargest(l):
    lar = l[0]
    slar = float('-inf')
    for i in range(0,len(l)):
        if (l[i]>lar):
            slar = lar
            lar = l[i]
        else:
            if (l[i]>slar):
                slar=l[i]
    return slar,lar

l=[32,534,67,65,7,6,45,56,56,67,3]
print(secondLargest(l))





