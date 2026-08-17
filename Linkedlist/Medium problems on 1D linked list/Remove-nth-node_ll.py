#Input:  5->1->2, N=2
#Output: 5->2
#Explanation: The 2nd node from the end of the linked list is 1. Therefore, we get this result after removing 1 from the linked list.





#Brute Force Approach

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:

    def length_ll(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count

    def del_node_n(self, head, n):

        # 1. Find position from start
        pos = self.length_ll(head) - n + 1

        # 2. Delete head node
        if pos == 1:
            return head.next

        # 3. Move till just before the node to delete
        curr = head
        count = 1
        while curr:
            if count == pos - 1:    # curr is BEFORE node to delete
                break
            curr = curr.next
            count += 1

        # 4. Delete the next node
        if curr and curr.next:
            curr.next = curr.next.next

        return head
    
    def print_ll(self, head):
        curr = head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

head = Node(1)
first=Node(2)
second=Node(3)
third=Node(4)
fifth=Node(5)
head.next = first
first.next = second
second.next = third
third.next = fifth
fifth.next = None

sol = Solution()
new_head = sol.del_node_n(head, 2)
sol.print_ll(new_head)



#Optimal Approach - Two Pointer Approach
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    




