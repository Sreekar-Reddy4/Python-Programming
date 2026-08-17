# Input: head -> 3 -> 7 -> 5 -> 7 -> 3

# Output: true

# Explanation: 37573 is a palindrome.



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def reverse_ll(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def palindrome_ll(self):
        if not self.head or not self.head.next:
            return True

        # find middle
        mid = self.middle_node()

        # reverse second half
        second = self.reverse_ll(mid)

        p1 = self.head
        p2 = second
        result = True

        while p2:
            if p1.data != p2.data:
                result = False
                break
            p1 = p1.next
            p2 = p2.next

        # optional restore second half (not necessary but clean)
        self.reverse_ll(second)

        return result

    def print_ll(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


SLL = LinkedList()
SLL.add_node(3)
SLL.add_node(7)
SLL.add_node(5)
SLL.add_node(7)
SLL.add_node(3)

print("Palindrome check:", SLL.palindrome_ll())
SLL.print_ll()
