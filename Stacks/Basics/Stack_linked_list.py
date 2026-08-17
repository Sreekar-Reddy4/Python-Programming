
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self,top=None):
        self.top=top
    
    def push(self,data):
        new_node = Node(data)
        new_node.next=self.top
        self.top=new_node
    
    def pop(self):
        if self.is_empty():
            return None
        
        result = self.top.data
        self.top = self.top.next
        return result
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self.top.data
    
    def size(self):
        count=0
        curr=self.top
        while curr:
            count+=1
            curr=curr.next
        return count
    
    def is_empty(self):
        return self.top is None

    def display(self):
        # elements = []
        curr = self.top
        while curr:
            print(curr.data)
            curr = curr.next
        

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack elements:", stack.display())  # Output: [30, 20, 10]
    print("Top element:", stack.peek())        # Output: 30
    print("Stack size:", stack.size())         # Output: 3
    print("Popped element:", stack.pop())      # Output: 30
    print("Stack elements after pop:", stack.display())  # Output: [20, 10]