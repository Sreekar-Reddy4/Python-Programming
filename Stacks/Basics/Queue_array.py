class ArrayQueue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.queue[0]
    
    def display(self):
        return self.queue


# Example usage:
if __name__ == "__main__":
    q = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue after enqueuing 1, 2, 3:", q.display())
    print("Dequeued item:", q.dequeue())
    print("Queue after dequeue:", q.display())
    print("Front item (peek):", q.peek())
    print("Is queue empty?", q.is_empty())
    print("Size of queue:", q.size())