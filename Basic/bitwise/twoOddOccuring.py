def TwoOddOccuring(arr, n):
    res = 0
    for i in range(n):
        res ^= arr[i]
    
    # Find the rightmost set bit in res
    set_bit_no = res & ~(res - 1)
    
    x = 0
    y = 0
    
    for i in range(n):
        if (arr[i] & set_bit_no) != 0:
            x ^= arr[i]
        else:
            y ^= arr[i]
    
    return x, y