## Before a given value code works evrey node except for first node i.e. head because before that there are no other nodes.

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
    
    def insert_node_before_gv(self,data,var):
        new_node = Node(data)
        prev = None
        current = self.head
        while current:
            prev = current
            current = current.next
            if current is None:
                print('No given value')
                return
            elif current.data==var:
                break
        
        new_node.next = prev.next 
        prev.next  = new_node
        return 
        
        

ll=LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)
ll.insert_node_before_gv(25,40)
ll.print_ll()
