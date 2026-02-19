def powerOfnumber(x,y):
    if y==0:
        return 1
    return x*powerOfnumber(x,y-1)

print(powerOfnumber(2,4))