ls=[10,30,45,23,65]

def average(ls):
    sum = 0
    for i in ls:
        sum =sum +i
    n=len(ls)
    average=sum/n
    return(average)
print(average(ls))