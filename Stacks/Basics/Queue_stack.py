

# Example 1:  
# Input:  
# ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]  
# [[], [4], [8], [], [], []]  
# Output: [null, null, null, 4, 8, false]  
# Explanation:  
# StackQueue queue = new StackQueue();  
# - queue.push(4);  
# - queue.push(8);  
# - queue.pop(); // returns 4  
# - queue.peek(); // returns 8  
# - queue.isEmpty(); // returns false  

# Example 2:  
# Input: 
# ["StackQueue", "isEmpty"]  
# [[]]  
# Output: [null, true]  
# Explanation:  
# StackQueue queue = new StackQueue();  
# - queue.isEmpty(); // returns true

class StackQueue:
    def __init__(self):
        # Initialize your data structure here
        self.input = []  # Stack to push elements
        self.output = [] # Stack to simulate FIFO order

    # Push element x to the back of queue
    def push(self, x: int):
        self.input.append(x)

    # Removes the element from in front of queue and returns that element
    def pop(self) -> int:
        # Shift input to output if output is empty
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        # If queue is still empty, return -1 (or throw an error if preferred)
        if not self.output:
            print("Queue is empty, cannot pop.")
            return -1

        return self.output.pop()

    # Get the front element
    def peek(self) -> int:
        # Shift input to output if output is empty
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        # If queue is still empty, return -1 (or throw an error if preferred)
        if not self.output:
            print("Queue is empty, cannot peek.")
            return -1

        return self.output[-1]

    # Returns true if the queue is empty, false otherwise
    def isEmpty(self) -> bool:
        return not self.input and not self.output


# Main function to test the StackQueue implementation
if __name__ == "__main__":
    commands = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
    q = StackQueue()
    # List of inputs
    inputs = [[], [4], [8], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            q.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(q.pop(), end=" ")
        elif commands[i] == "peek":
            print(q.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if q.is_empty() else "false", end=" ")
        elif commands[i] == "StackQueue":
            print("null", end=" ")