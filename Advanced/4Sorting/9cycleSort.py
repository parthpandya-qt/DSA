def cycleSort(arr):
    swaps=0
    for i in range(len(arr)-1):
        item=arr[i]
        pos=i
        for j in range(i+1,len(arr)):
            if arr[j]<item:
                pos+=1
        if pos==i:
            continue
        while item==arr[pos]:
            pos+=1
        arr[pos] , item = item , arr[pos]
        swaps+=1
        while pos!=i:
            pos=i
            for j in range(i+1,len(arr)):
                if arr[j]<item:
                    pos+=1
                if pos==i:
                    continue
            while item==arr[pos]:
                pos+=1
            arr[pos],item = item,arr[pos]
            swaps+=1
        return swaps
arr = [20, 40, 50, 10, 30]
print(cycleSort(arr))
print(arr) 



