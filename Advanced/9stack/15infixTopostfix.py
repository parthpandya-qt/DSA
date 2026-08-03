def infixToPostfix(exp):

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    stack = []
    result = []

    for ch in exp:

        # Operand
        if ch.isalnum():
            result.append(ch)

        # Left parenthesis
        elif ch == '(':
            stack.append(ch)

        # Right parenthesis
        elif ch == ')':

            while stack and stack[-1] != '(':
                result.append(stack.pop())

            stack.pop()      # Remove '('

        # Operator
        else:

            while (stack and
                   stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[ch] or
                    (precedence[stack[-1]] == precedence[ch] and ch != '^'))):

                result.append(stack.pop())

            stack.append(ch)

    # Pop remaining operators
    while stack:
        result.append(stack.pop())

    return ''.join(result)



