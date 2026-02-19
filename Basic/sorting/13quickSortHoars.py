def hoars(arr,l,h):
    i=l-1
    j=h+1
    pivot=arr[l]
    while True:
        i+=1
        while arr[i]<pivot :
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if(i>=j):
            return j
        arr[i],arr[j]=arr[j],arr[i]        



def quickSort(arr,l,h):
    if l<h:
        p=hoars(arr,l,h)
        quickSort(arr,l,p)
        quickSort(arr,p+1,h)

arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, len(arr) - 1)
print(arr)