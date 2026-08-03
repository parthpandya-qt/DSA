class KStack:

    def __init__(self, n, k):
        self.n = n
        self.k = k

        # Stores the actual elements
        self.arr = [None] * n

        # Stores the index of the top element of each stack
        self.top = [-1] * k

        # Used for both:
        # 1. Linking elements within a stack
        # 2. Maintaining the free list
        self.next = [i + 1 for i in range(n)]
        self.next[n - 1] = -1

        # Points to the first free index
        self.freeTop = 0

    def isFull(self):
        return self.freeTop == -1

    def isEmpty(self, sn):
        return self.top[sn] == -1

    def push(self, sn, x):

        # Overflow check
        if self.isFull():
            raise Exception("Stack Overflow")

        # Get the first free index
        i = self.freeTop

        # Move freeTop to the next free location
        self.freeTop = self.next[i]

        # Insert the element
        self.arr[i] = x

        # Link the new element with the previous top
        self.next[i] = self.top[sn]

        # Make the new element the top of this stack
        self.top[sn] = i

    def pop(self, sn):

        # Underflow check
        if self.isEmpty(sn):
            raise Exception("Stack Underflow")

        # Get the current top index
        i = self.top[sn]

        # Move the stack top to the next element
        self.top[sn] = self.next[i]

        # Add the removed index back to the free list
        self.next[i] = self.freeTop

        # Update freeTop
        self.freeTop = i

        # Return the popped element
        return self.arr[i]

    def peek(self, sn):

        if self.isEmpty(sn):
            raise Exception("Stack is Empty")

        return self.arr[self.top[sn]]