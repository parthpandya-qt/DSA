def maxAppearing(left,right):
    max_val=max(right)
    freq=[0]*max_val+2
    n=len(left)
    for i in range(n):
        freq[left[i]]+=1
        freq[right[i]+1]-=1
    max_freq=freq[0]
    res=0
    for i in range(1,max_val+1):
        freq[i]+=freq[i-1]
        if freq[i]>max_freq:
            max_freq=freq[i]
            res=i
    return res





def maxAppearence(l,r):
    maxElement = max(r)
    freq = [0]*(maxElement+2)

    n=len(l)
    for i in range(n):
        freq[l[i]]+=1
        freq[r[i]+1]-=1
    maxFreq=freq[0]
    res = 0
    for i in range(1,len(freq)):
        freq[i] = freq[i-1]+freq[i]
        if freq[i]>maxFreq:
            maxFreq = freq[i]
            res = i
    return res




