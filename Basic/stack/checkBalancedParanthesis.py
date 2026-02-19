def isMatching(a,b):
    if (a=='(' and b==')') or (a=='{' and b=='}') or (a=='[' and b==']'):
        return True
    else:
        return False
    
def isBalanced(str):
    stack=[]
    for i in str:
        if i in ('(','{','['):
            stack.append(i)
        else:
            if not stack:
                return False
            elif (isMatching(stack[-1],i)==False):
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False                    
    

print(isBalanced("[{}])"))