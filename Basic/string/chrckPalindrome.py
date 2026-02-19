# def isPalindrome(x):
#     rev=''
#     for i in x:
#         rev = i+rev
#         if rev==x:
#             return True
#     return False

# print(isPalindrome("aabs"))    
def isPalindrome(x):
    x=str(x)
    low=0
    high=len(x)-1
    while low<=high:
        if x[low]!=x[high]:
            print("No")
            break
        low+=1
        high-=1
    else:
        print("Yes")     

isPalindrome(12344321)        