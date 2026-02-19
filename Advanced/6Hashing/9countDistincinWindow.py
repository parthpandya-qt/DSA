# def countDistict(arr,k):
#     Sum=0
#     n=len(arr)
#     count=1
#     for i in range(n-k+1):
#         print(len(set(arr[i:i+k])))
            
def countDistict(arr,k):
    n=len(arr)
    hashMap={}
    for i in range(k):
        if arr[i] in hashMap:
            hashMap[arr[i]]+=1
        else:
            hashMap[arr[i]]=1
    for i in range(k,n):
        x=arr[i-k]
        hashMap[x]-=1
        if hashMap[x]==0:
            del(hashMap[x])
        
        if arr[i] in hashMap:
            hashMap[arr[i]] += 1
        else:
            hashMap[arr[i]] = 1
        print(len(hashMap))
        