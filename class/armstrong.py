def armStrong(num):
    n = 0
    original = num
    newnum = 0
    while num>0:
        remaining = num%10
        num = num//10
        
        newnum += remaining**3
    if newnum == original:
        return True
    else:
        return False

print(armStrong(353))