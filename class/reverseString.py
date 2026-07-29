def reverse(str):
    str1 = ""
    j = len(str)-1
    while j>=0:
        str1+=str[j]
        j-=1
    return str1
print(reverse("parth"))
