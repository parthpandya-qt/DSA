# def leftOccurence(x):
#     count=[0]*254
#     for i in range(len(x)):
#         count[ord(x[i])]+=1
#     for i in range(len(x)):
#         if (count[ord(x[i])]>1)    :
#             return i
#     return -1   

# print(leftOccurence("aaddcc"))
def leftOccurence(x):
    visited=[False]*256
    res=-1
    for i in range(len(x)-1,-1,-1):
        if visited[ord(x[i])]==True:
            res = i
        else:
            visited[ord(x[i])]==True
    return res        