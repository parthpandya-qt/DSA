def odd(n):
    res=0
    for i in n:
        res=res^i
    return res

print(odd([12,12,12,23,23,45,45]))
    