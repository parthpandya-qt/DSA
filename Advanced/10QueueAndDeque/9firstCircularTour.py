def firstCircularTour(petrol,distance):
    start=0
    curr_petrol=0
    prev_petrol=0
    n=len(petrol)
    for i in range(n):
        curr_petrol+=petrol[i]-distance[i]
        if curr_petrol<0:
            start=i+1
            prev_petrol+=curr_petrol
            curr_petrol=0
    if curr_petrol+prev_petrol>=0:
        return start+1
    else:
        return -1