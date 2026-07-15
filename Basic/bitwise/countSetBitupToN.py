def countBit(n):
    if(n==0):
        return 0
    def largestPowerOf2(n):
        p = 0
        while (1 << p) <= n:
            p += 1
        return p - 1
    largestPower = largestPowerOf2(n)
    if largestPower == 0:
        return 1
    upTolargestPower = (largestPower * (1 << (largestPower - 1)))
    afterlargestPower = n - (1 << largestPower) + 1
    return upTolargestPower + afterlargestPower + countBit(n - (1 << largestPower))