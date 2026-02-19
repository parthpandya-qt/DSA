def linearSearch(l,x):
    for i in range (0,len(l)):
        if(l[i]==x):
            return i
    return -1

l=[23,34,56,567,34,2,3,4,5,6,7,8,9,]        
x=4

print(linearSearch(l,x))