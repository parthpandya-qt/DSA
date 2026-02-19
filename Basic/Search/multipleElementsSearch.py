def linearSearchAll(l, x):
    indices = [0] * len(l) 
    count = 0
    for i in range(len(l)):
        if l[i] == x:
            indices[count] = i
            count += 1
    return indices[:count]  

# Example
l = [23, 34, 56, 567, 34, 2, 3, 4, 5, 6, 7, 8, 9]
x = 34
print(linearSearchAll(l, x))  
