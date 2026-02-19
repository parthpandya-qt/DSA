def isSorted(l):
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            return False
    return True

        
l=[1,2,4,7,7]
print(isSorted(l))        