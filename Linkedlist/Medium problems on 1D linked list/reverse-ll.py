#Given the head of a singly linked list. Reverse the given linked list and return the head of the modified list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev         # Update head to new first node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print("Original Linked List:")
ll.print_list()
ll.reverse()
print("Reversed Linked List:")
ll.print_list()