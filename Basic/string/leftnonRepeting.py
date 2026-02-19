def nonReapetingleft(x):
    count=[0]*256
    for i in range(len(x)):
        count[ord(x[i])]+=1
    for i in range(len(x)):
        if count[ord(x[i])]==1:
            return i
    return -1    

print(nonReapetingleft("aabbcdsghj"))