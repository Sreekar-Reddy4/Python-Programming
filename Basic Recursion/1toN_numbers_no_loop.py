# Print numbers from 1 to n without the help of loops. (print the number from 1 to n recursively.)

# 1. using recursive call stack   Time complexity: O(n), Space Complexity: O(n) (due to recursive call stack).

def printNos(n):
    if n == 0:
        return
    printNos(n - 1)  # Recursive call for smaller value
    print(n, end=" ")  # Print current number

n = 10
printNos(n)

# 2. Using Tail Recursion (to avoid extra stack space)
def printNosTail(n, i=1):
    if i > n:
        return
    print(i, end=" ")
    printNosTail(n, i + 1)

n = 10
printNosTail(n)
 
