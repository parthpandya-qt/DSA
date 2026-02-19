def digit(n):
    if(n<10):
        return n
    else:
        return n%10 + digit(n//10)

print(digit(1234))    