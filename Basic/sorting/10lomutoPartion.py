def lomuto(arr,l,h):
    i=l-1
    pivot=arr[h]
    for j in range(l,h):
        if(arr[j]<=pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1        

arr = [10, 80, 30, 90, 40, 50, 70]
p = lomuto(arr, 0, len(arr) - 1)
print("Partition index:", p)
print("Array after partition:", arr)



# The Lomuto partition is a partitioning method used in Quick Sort. It chooses the last element as the pivot and rearranges the array so that:

# All elements less than or equal to the pivot are on the left.
# All elements greater than the pivot are on the right.
# The pivot ends up in its correct sorted position.