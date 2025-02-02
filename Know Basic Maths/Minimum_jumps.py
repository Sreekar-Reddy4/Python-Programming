# You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

# For example: (Medium - Level)

# If arr[i] = 3, you can jump 1 step, 2 steps, or 3 steps forward from position i.
# If arr[i] = 0, you cannot jump forward from that position.
# Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

# Note:  Return -1 if you can't reach the end of the array.

# 1. Brute Force Approach Time Complexity: O(2**n), Space Complexity: O(n)

import sys

def minJumpsRecursive(arr, current, n):
    # If we have reached the last index
    if current >= n - 1:
        return 0

    # If element at current index is 0, we cannot move forward
    if arr[current] == 0:
        return sys.maxsize  # Representing Infinity

    # Try all possible jumps from current position
    min_jumps = sys.maxsize
    for jump in range(1, arr[current] + 1):
        jumps = minJumpsRecursive(arr, current + jump, n)
        if jumps != sys.maxsize:
            min_jumps = min(min_jumps, jumps + 1)

    return min_jumps

def minJumps(arr):
    result = minJumpsRecursive(arr, 0, len(arr))
    return result if result != sys.maxsize else -1  # Return -1 if not possible

# Example Usage
arr = [2, 3, 1, 1, 4]
print(minJumps(arr))  # Output: 2


# 2. Memoization Approach Time Complexity: O(n**2), Space Complexity: O(n)

import sys

def minJumpsMemo(arr, current, n, dp):
    if current >= n - 1:
        return 0
    if arr[current] == 0:
        return sys.maxsize

    if dp[current] != -1:
        return dp[current]

    min_jumps = sys.maxsize
    for jump in range(1, arr[current] + 1):
        jumps = minJumpsMemo(arr, current + jump, n, dp)
        if jumps != sys.maxsize:
            min_jumps = min(min_jumps, jumps + 1)

    dp[current] = min_jumps
    return dp[current]

def minJumps(arr):
    n = len(arr)
    dp = [-1] * n
    result = minJumpsMemo(arr, 0, n, dp)
    return result if result != sys.maxsize else -1

arr = [2, 3, 1, 1, 4]
print(minJumps(arr))  # Output: 2


# 3. Optimal Force Approach Time Complexity: O(n), Space Complexity: O(1)
def minJumps(arr):
    n = len(arr)
    
    # If array has only one element, we are already at the last position
    if n == 1:
        return 0
    
    # If first element is 0, we can't move anywhere
    if arr[0] == 0:
        return -1
    
    maxReach = arr[0]  # Farthest we can reach
    steps = arr[0]      # Steps we can still take
    jumps = 1           # Number of jumps

    for i in range(1, n):
        # If we reach the last index, return jumps
        if i == n - 1:
            return jumps
        
        maxReach = max(maxReach, i + arr[i])  # Update the farthest we can reach
        steps -= 1  # Use a step
        
        # If steps become zero, we must jump
        if steps == 0:
            jumps += 1
            # If we can't move forward, return -1
            if i >= maxReach:
                return -1
            steps = maxReach - i  # Update steps
    
    return -1  # If we exit the loop, we couldn't reach the end
