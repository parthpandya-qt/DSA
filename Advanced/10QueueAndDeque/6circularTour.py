def circularTour(petrol,distance):
    n=len(petrol)
    for start in range(n):
        end=start
        
        curr_petrol=0
        while True:
            curr_petrol+=(petrol[end]-distance[end])
            if curr_petrol<0:
                break
            end=(end+1)%n
            if end==start:
                return start+1
    return -1