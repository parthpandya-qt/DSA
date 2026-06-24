def subset(string,curr,ind):
    if len(string)==ind:
        print(curr,end=" ")
        return
    subset(string,curr,ind+1)
    subset(string,curr+string[ind],ind+1)
subset("abc", "", 0)



