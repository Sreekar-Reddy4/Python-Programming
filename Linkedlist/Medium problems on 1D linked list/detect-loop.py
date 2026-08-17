# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1

# Output: true

# Explanation: The tail of the linked list connects to the node at 1st index.






#Brute Force Approach
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class solution:
    
    def detect_loop(self,head):
        curr=head
        d={}
        while curr:
            if curr in d:
                return True
            d[curr]=1
            curr=curr.next
        return None

sol = solution()
head=Node(1)
first=Node(2)
second=Node(3)
third=Node(4)
fifth=Node(5)

head.next = first
first.next = second
second.next = third
third.next = fifth
fifth.next = first

print(sol.detect_loop(head))







#Optimal Approach - Floyd's Cycle Detection Algorithm


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # move 1 step
        fast = fast.next.next     # move 2 steps

        if slow == fast:
            return True           # loop exists

    return False                  # no loop


# ---------------------
# Create a small list
# ---------------------
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
# create loop
d.next = b   # loop back to node b

# Test
print(detect_loop(a))   # True
