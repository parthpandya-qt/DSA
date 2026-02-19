def isPal(digit):
    original = digit
    rev = 0
    while digit > 0:
        pal = digit % 10
        rev = rev * 10 + pal
        digit = digit // 10
    if rev == original:
        return "yes it is palindrome"
    else:
        return "it is not a palindrome"

print(isPal(5005))

