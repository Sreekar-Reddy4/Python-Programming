class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear  = None
    
    def enqueue(self,data):
        new_node = Node(data)
        
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front is None :
            print('Queue is empty')
            return None
        temp = self.front
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        return temp.data
    
    def peek(self):
        if self.front is None :
            print('Queue is empty')
            return None
        
        temp = self.front
        return temp.data
    
    def size(self):
        count=0
        temp=self.front
        while temp:
            count+=1
            temp=temp.next
        return temp

    def is_empty(self):
        return self.front is None
    
    def display(self):
        curr = self.front
        while curr:
            print(curr.data)
            curr = curr.next

if __name__ == "__main__":
    queue = Queue_LL()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue elements:")
    queue.display()  # Output: 10, 20, 30
    print("Front element:", queue.peek())        # Output: 10
    print("Queue size:", queue.size())           # Output: 3
    print("Dequeued element:", queue.dequeue())  # Output: 10
    print("Queue elements after dequeue:")
    queue.display()  # Output: 20, 30