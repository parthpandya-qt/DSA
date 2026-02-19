ls=[21,32,43,54,65,76,87,98,12,23,34,45,56,67,78,89]

def segrigate(ls):
    even=[]
    odd=[]
    for i in ls:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)    
    return odd,even

print(segrigate(ls))