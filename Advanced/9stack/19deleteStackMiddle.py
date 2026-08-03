def deleteMiddle(stack):

    n = len(stack)

    def solve(k):

        if k == 0:
            stack.pop()
            return

        x = stack.pop()

        solve(k - 1)

        stack.append(x)

    solve(n // 2)