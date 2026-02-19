def lomuto(arr,l,h):
    i=l-1
    pivot=arr[h]
    for j in range(l,h):
        if(arr[j]<=pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1 

def quickSort(arr,l,h):
    if l<h:
        p=lomuto(arr,l,h)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,h)

arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, len(arr) - 1)
print(arr)