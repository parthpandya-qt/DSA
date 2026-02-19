def largestElement(ls):
    res=ls[0]
    for i in range(1,len(ls)):
        if(ls[i]>res):
            res=ls[i]
    return res

ls=[233,45,543,64,654,2,43,43]
print(largestElement(ls))
        
                