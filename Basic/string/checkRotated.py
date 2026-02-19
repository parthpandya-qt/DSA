def rotate(x,y):
    for i in range(len(x)):
        rotated = x[i:] + x[:i]
        if y== rotated:
            return True
    return False 
                               