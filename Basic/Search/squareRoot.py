def squareRoot(x):
    low=0
    high=x
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        msq=mid*mid
        if(msq==x):
            return mid
        elif(msq>x):
            high=mid-1
        else:
            low=mid+1
            ans=mid
    return ans            
                                 
