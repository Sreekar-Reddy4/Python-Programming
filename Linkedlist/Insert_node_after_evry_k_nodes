#FIRST: The Core Rule
#👉 A single node cannot appear in two places in a linked list.
#Why?
#Because:
#A node has one next pointer
#If you attach it somewhere else, its previous connection is destroyed

Insert a node every time ‘k’ nodes
Example:
Input: 1 → 2 → 3 → 4 → 5 → 6
k = 2
Insert “X” after every 2 nodes
Output: 1 → 2 → X → 3 → 4 → X → 5 → 6 → X

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self,head=None):
        self.head = head
    
    def add_node(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def insert_k_nodes(self,k,data):
        current = self.head
        count = 0
        prev = None
        while current:
            prev=current
            count+=1
            current=current.next
            if count == k:
                new_node = Node(data)
                new_node.next = prev.next
                prev.next = new_node
                count=0
    
    def print_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        

SL = SLL()
SL.add_node(1)
SL.add_node(2)
SL.add_node(3)
SL.add_node(4)
SL.add_node(5)
SL.add_node(6)
SL.insert_k_nodes(2,'X')
SL.print_ll()
