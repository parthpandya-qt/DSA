def bubbleSort(l):
    n=len(l)
    for i in range(n-1):
        swapped =False
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped=True
        if not swapped:
            break
    return l
print(bubbleSort([23,54,2,34,32,1,23,43]))                




