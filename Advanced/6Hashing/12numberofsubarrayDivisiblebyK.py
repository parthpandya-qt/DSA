def subArray(arr,k):
    hashMap = {0:1}
    prefixSum = 0
    res = 0
    for i in arr:
        prefixSum += i
        remainder = prefixSum % k
        if remainder in hashMap:
            res += hashMap[remainder]
            hashMap[remainder] += 1
        else:
            hashMap[remainder] = 1
       
            
    return res