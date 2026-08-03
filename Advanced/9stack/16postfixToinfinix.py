def evaluatePostfix(exp):

    stack = []

    for ch in exp:

        if ch not in ['+', '-', '*', '/', '^']:
            stack.append(int(ch))

        else:

            op2 = stack.pop()
            op1 = stack.pop()

            if ch == '+':
                result = op1 + op2

            elif ch == '-':
                result = op1 - op2

            elif ch == '*':
                result = op1 * op2

            elif ch == '/':
                result = int(op1 / op2)

            elif ch == '^':
                result = op1 ** op2

            stack.append(result)

    return stack[-1]