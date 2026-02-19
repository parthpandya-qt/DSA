def prefixEvaluation(exp):
    res=[]
    stack=[]
    exp=exp[::-1]
    for ch in exp:
        if ch not in ['+','-','/','*','^']:
            stack.append(ch)
        else:
            op1=int(stack.pop())
            op2=int(stack.pop())
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
