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
    
    def delete_node(self, value):
    current = self.head
    prev = None

    # Case 1: List is empty
    if not current:
        print("List is empty")
        return
    
    # Case 2: First node is the node to delete
    if current.data == value:
        self.head = current.next
        return

    # Case 3: Search for the node to delete
    while current and current.data != value:
        prev = current
        current = current.next

    # Case 4: Value not found
    if current is None:
        print("Value not found")
        return

    # Case 5: Delete the node
    prev.next = current.next

    
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
