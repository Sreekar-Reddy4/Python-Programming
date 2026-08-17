# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1

# Output(value of the returned node is displayed): 2

# Expla﻿nation: The tail of the linked list connects to the node at 1st index.

#Brute Force Approach using Hashing
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class solution:
    
    def startingpt_loop(self,head):
        curr=head
        d={}
        while curr:
            if curr in d:
                return curr
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

print(sol.startingpt_loop(head))



#Optimal Approach using Floyd's Cycle Detection Algorithm
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class solution:

    def startingpt_loop(self,head):
        slow=head
        fast=head
        
        #Detecting Loop
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
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
print(sol.startingpt_loop(head))