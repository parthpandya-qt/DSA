import string

def convert_case(str):
    alpha = string.ascii_lowercase
    str1 = ""
    for i in str:
        if i in alpha:
            str1+=i.upper()
        else:
            str1+=i.lower()
    return str1