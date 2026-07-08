def Reverse(l):
    start = 0
    end = len(l)-1
    while start <= end :
        l[start],l[end]=l[end],l[start]
        start+=1
        end-=1
    return l
l=[1,2,3,4,5,6,7,8,9]
print(Reverse(l))


