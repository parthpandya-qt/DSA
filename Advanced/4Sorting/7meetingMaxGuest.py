def meetingMaxGurst(arrival,departure):
    arrival.sort()
    departure.sort()
    i,j=0,0
    curr,res=1,1
    n=len(arrival)
    while i<n and j<n:
        if arrival[i]<=departure[j]:
            curr+=1
            i+=1
        else:
            curr-=1
            j+=1
        res=max(res,curr)
    return res

print(meetingMaxGurst([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000]))
