def median(nums1,nums2):
    if len(nums1)>len(nums2):
        nums1,nums2=nums2,nums1
    n1=len(nums1)
    n2=len(nums2)
    l,r=0,n1
    total=n1+n2
    while l<=r:
        i1=(r+l)//2
        i2=(n1+n2+1)//2-i1
        
        left1 = float("-inf") if i1 == 0 else nums1[i1 - 1]
        right1 = float("inf") if i1 == n1 else nums1[i1]
        left2 = float("-inf") if i2 == 0 else nums2[i2 - 1]
        right2 = float("inf") if i2 == n2 else nums2[i2]

        if left1<=right2 and left2<=right1:
            if total %2 ==0:
                return (max(left1,left2)+min(right1,right2))/2
            else:
                return max(left1,left2)
        elif left1>right2:
            r=i1-1
        else:
            l=i1+1


        