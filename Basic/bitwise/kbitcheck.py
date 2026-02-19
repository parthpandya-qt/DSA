def kbitcheck(n,i):
    if n & (1<<(i-1)):
        return True
    else:
        return False

print(kbitcheck(5,1))