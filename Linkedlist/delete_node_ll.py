class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def delete_node(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            print("Key not found in the list.")
        
        prev.next = current.next
        current = None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = Linkedlist()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)
ll.add_node(50)
ll.delete_node(30)
ll.print_list()  