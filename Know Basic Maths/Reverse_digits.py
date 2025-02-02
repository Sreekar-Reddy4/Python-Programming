# Given an integer N return the reverse of the given number.

# Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

# 1. Optimal Approach -> Time Complexity: O(log10N + 1), Space Complexity: O(1)

n = int(input("Enter an integer: "))
revNum = 0

while n > 0:
    
    lstdgt = n % 10
    
    revNum = (revNum * 10) + lstdgt
    
    n = n // 10
# Print the reversed number.
print(revNum)