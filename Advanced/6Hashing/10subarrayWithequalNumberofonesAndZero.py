def subArrayWithEqualNumberOfOnesAndZeros(arr):
    # Convert 0 to -1
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1

    hashMap = {0: 1}
    prefixSum = 0
    res = 0

    for num in arr:
        prefixSum += num

        if prefixSum in hashMap:
            res += hashMap[prefixSum]
            hashMap[prefixSum] += 1
        else:
            hashMap[prefixSum] = 1

    return res