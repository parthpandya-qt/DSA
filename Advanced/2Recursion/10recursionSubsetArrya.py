def subset(arr,temp=[],i=0):
    if i == len(arr):
        print(temp)
        return 

    subset(arr,temp,i+1)
    subset(arr,temp + [arr[i]],i+1)

print(subset([1,2]))