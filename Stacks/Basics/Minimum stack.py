# problem Statement: Design a stack that supports the following operations in constant time: push, pop, top, and retrieving the minimum element.

# Implement the MinStack class:

# MinStack(): Initializes the stack object.
# void push(int val): Pushes the element val onto the stack.
# void pop(): removes the element on the top of the stack.
# int top(): gets the top element of the stack.
# int getMin(): retrieves the minimum element in the stack.

class MinStack:
    # Empty Constructor
    def __init__(self):
        # Initialize a stack
        self.st = []

    # Method to push a value in stack
    def push(self, value):
        # If stack is empty
        if not self.st:
            # Push current value as minimum
            self.st.append((value, value))
            return

        # Update the current minimum
        mini = min(self.getMin(), value)

        # Add the pair to the stack
        self.st.append((value, mini))

    # Method to pop a value from stack
    def pop(self):
        # Using in-built pop method
        self.st.pop()

    # Method to get the top of stack
    def top(self):
        # Return the top value
        return self.st[-1][0]

    # Method to get the minimum in stack
    def getMin(self):
        # Return the minimum
        return self.st[-1][1]

if __name__ == "__main__":
    s = MinStack()
    
    # Function calls
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin(), end=" ")
    s.pop()
    print(s.top(), end=" ")
    s.pop()
    print(s.getMin())