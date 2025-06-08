### Inserting new node at begining of linked list

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
    
    def insert_node_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data,end = " ")
            current = current.next
        print(None)
    
l1 = Linkedlist()
l1.add_node(10)
l1.add_node(20)
l1.add_node(30)
l1.add_node(40)
l1.insert_node_begining(5)
l1.display()