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
    
    def len_ll(self):
        count=0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count

l1 = Linkedlist()
l1.add_node(10)
l1.add_node(20)
l1.add_node(30)
l1.add_node(40)
print(l1.len_ll())