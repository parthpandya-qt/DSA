def largestElement(ls):
    res=ls[0]
    for i in range(1,len(ls)):
        if(ls[i]>res):
            res=ls[i]
    return res

ls=[233,45,543,64,654,2,43,43]
print(largestElement(ls))





def largest(arr, n):
    
    if n == 1:
        return arr[0]

    
    max_rest = largest(arr, n - 1)

    
    if arr[n - 1] > max_rest:
        return arr[n - 1]
    else:
        return max_rest


arr = [10, 25, 7, 89, 45]
print("Largest element:", largest(arr, len(arr)))