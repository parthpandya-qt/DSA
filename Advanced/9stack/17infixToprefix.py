def infixPrefix(exp):
    exp=exp[::-1]
    hashMap={
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3}
    stack=[]
    result=[]
    for ch in exp:
        if ch.isalnum():
            result.append(ch)
        elif ch==')':
            stack.append(ch)
        elif ch=='(':
            while stack and stack[-1]!=')':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1]!=')' and hashMap[ch]<hashMap[stack[-1]]:
                result.append(stack.pop())
            stack.append(ch)
    while stack:
        result.append(stack.pop())
    return ''.join(result[::-1])
    
    
         
