def sub(x,y):
    if x>y:
        while y>0:
            x=x-1
            y=y-1
        return x
    else:
        while x>0:
            y=y-1
            x=x-1
        return y

print(sub(23,22))


print(sub(2,45))


