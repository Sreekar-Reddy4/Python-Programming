class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class solution:
    def length_of_loop(self, head):
        d = {}
        curr = head
        count = 1
        while curr:
            if curr in d:
                return count - d[curr]
            else:
                d[curr] = count
            count += 1
            curr = curr.next
        return 0

# Example usage:
if __name__ == "__main__":
    # Creating a linked list with a loop for testing
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

    sol = solution()
    print("Length of loop is:", sol.length_of_loop(head))  


#Optimal Approach - Floyd's Cycle Detection Algorithm to find length of loop
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class solution:
    
    def length_loop(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return self.findlength(slow,fast)
        return None
    
    def findlength(self,slow,fast):
        count=1
        fast=fast.next
        while slow!=fast:
            count+=1
            fast=fast.next
        return count


if __name__ == "__main__":
    # Creating a linked list with a loop for testing
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

    sol = solution()
    print("Length of loop is:", sol.length_of_loop(head))  
