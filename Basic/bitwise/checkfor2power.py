def check(n):
    if n&(n-1)==0:
        return True
    return False

print(check(9))