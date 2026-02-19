def division(x, y):
    '''Only enter divisible numbers'''
    count = 0
    while x >= y:
        x = x - y
        count += 1
    return count