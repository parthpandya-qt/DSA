def postfixToinfinix(exp):
    res=[]
    stack=[]
    
    for ch in exp:
        if ch not in ['+','-','/','*','^']:
            stack.append(ch)
        else:
            op2=int(stack.pop())
            op1=int(stack.pop())
            if ch=='+':
                result=op1+op2
            elif ch=='-':
                result=op1-op2
            elif ch=='*':
                result=op1*op2
            elif ch=='/':
                result=op1/op2
            elif ch=='^':
                result=op1**op2
            stack.append(result)
    return stack[-1]
