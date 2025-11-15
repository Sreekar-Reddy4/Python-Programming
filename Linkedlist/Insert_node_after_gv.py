### Insert node after a given value will be applicable to all nodes from first to last.
Insert a node after a given value

Example:
Insert 25 after the node with value 20
Input: 10 → 20 → 30 → 40
Output: 10 → 20 → 25 → 30 → 40

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def add_node(self,var):
        new_node = Node(var)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            return 
    
    def print_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    def insert_node_after_gv(self,data,var):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data==var:
                break
            current = current.next
            
        if current is None:
            print('No given value')
            return
        
        
        new_node.next = current.next
        current.next = new_node
        return      

ll=LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)
ll.insert_node_after_gv(25,40)
ll.print_ll()
