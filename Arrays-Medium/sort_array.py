#Dutch National fla algorithm
# Problem Statement:
# Given an array consisting of three types of elements (e.g., 0s, 1s, and 2s), the goal is to sort them in a single traversal (O(n) time complexity) without using extra space.

# Approach:
# The algorithm uses three pointers:

# Low (l) – Marks the boundary for 0s (red).

# Mid (m) – Traverses the array and decides where elements should go.

# High (h) – Marks the boundary for 2s (blue).

# Algorithm Steps:

# Initialize:

# low = 0, mid = 0, and high = n - 1 (last index).

# Iterate while mid <= high:

# If arr[mid] == 0: Swap arr[mid] and arr[low], then increment low and mid.

# If arr[mid] == 1: Increment mid (1s are already in the correct place).

# If arr[mid] == 2: Swap arr[mid] and arr[high], then decrement high (don't increment mid immediately as the swapped element needs to be checked).


def sort_array(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
    return arr

sol = sort_array([2, 0, 1, 2, 1, 0, 0, 1, 2])
print(sol)