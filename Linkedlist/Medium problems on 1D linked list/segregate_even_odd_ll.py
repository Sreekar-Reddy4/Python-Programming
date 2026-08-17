# Input: 1→2→3→4→5→6→Null
# Output: 2→4→6→1→3→5→Null
# Explanation : Odd Nodes in LinkedList are 1,3,5 and Even Nodes in LinkedList are 2,4,6
# In Modified LinkedList all even Nodes comes before all Odd Nodes. So Modified LinkedList looks like 2→4→6→1→3→5→Null. Order of even and odd Nodes is 
# maintained in modified LinkedList.

# Input: 1→3→5→Null
# Output: 1→3→5→Null
# Explanation: As there are no Even Nodes in LinkedList, The Modified LinkedList is same as Original LinkedList.


# Node definition for singly-linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:

    # Function to segregate even and odd nodes in a linked list
    def segregateEvenOdd(self, head):

        # Edge case: If list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Create pointers for the heads and tails of even and odd lists
        evenHead = evenTail = None
        oddHead = oddTail = None

        # Pointer to traverse the list
        current = head

        # Traverse the linked list
        while current:

            # If the current node has even value
            if current.data % 2 == 0:
                if not evenHead:
                    evenHead = evenTail = current
                else:
                    evenTail.next = current
                    evenTail = current

            else:
                # If the current node has odd value
                if not oddHead:
                    oddHead = oddTail = current
                else:
                    oddTail.next = current
                    oddTail = current

            # Move to next node
            current = current.next

        # If no even nodes found, return odd list
        if not evenHead:
            return oddHead

        # If no odd nodes found, return even list
        if not oddHead:
            return evenHead

        # Combine even and odd lists
        # evenTail.next = oddHead
        oddTail.next=evenHead

        # Set end of list to null
        evenTail.next = None

        return oddHead

# Driver code
def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

sol = Solution()
newHead = sol.segregateEvenOdd(head)
printList(newHead)
