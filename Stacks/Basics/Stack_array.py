# Problem Statement: Implement a Last-In-First-Out (LIFO) stack using an array. 
# The implemented stack should support the following operations: push, pop, peek, and isEmpty.

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,item):
        """Add an item to the top of the stack."""
        self.stack.append(item)
    
    def pop(self):

        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    
    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

# Example usage:
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())  # Output: 3
    print(s.pop())   # Output: 3
    print(s.isEmpty())  # Output: False
    print(s.pop())   # Output: 2
    print(s.pop())   # Output: 1
    print(s.isEmpty())  # Output: True
