def find(arr1,arr2):
    
    sum1 = 0
    sum2 = 0
    for i in arr1:
        sum1+=i
    for j in arr2:
        sum2+=j
    return abs(sum1-sum2)


def find(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    hashMap={}
    if n<m:
        arr1,arr2=arr2,arr1
    for i in arr1:
        if i in hashMap:
            hashMap[i]+=1
        else:
            hashMap[i]=1
    for j in arr2:
        if j in hashMap:
            if hashMap[j]==0:
                del hashMap[j]
            hashMap[j]-=1
    if hashMap:
        return list(hashMap.keys())[0]
        
#you are given two arr length of arr1 is n and arr2 is n+1 they have same element only 

    
