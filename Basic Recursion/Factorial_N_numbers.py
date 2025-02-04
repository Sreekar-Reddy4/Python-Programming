# Given a number X,  print its factorial.

# 1. Using loops Time Complexity: O(n), Space Complexity: O(1)
n=5
fact = 1
for i in range(n,1,-1):
    if n > 1:
        fact = fact * i
print(fact)     

# 2. Using Recursion Time Complexity: O(n), Space Complexity: O(n)
n=6
def fact(n):
    if n>1:
        return n * fact(n-1)
    return 1
print(fact(n))  


        
    
    