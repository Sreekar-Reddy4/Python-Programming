# You are given an array. The task is to reverse the array and print it. 
# 1. Using extra array  Time Complexity: O(n), Space Complexity: O(n)

def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")


def reverseArray(arr, n):
    ans = [0] * n
    for i in range(n - 1, -1, -1):     # ans = arr[::-1]  # Reverse using slicing
        ans[n - i - 1] = arr[i]
    printArray(ans, n)

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)

# 2.  Space-optimized iterative method (using pointers)  Time Complexity: O(n), Space Complexity: O(1)
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")

def reverseArray(arr, n):
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    printArray(arr, n)

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)

# 3. Using Recursion  Time Complexity: O(n), Space Complexity: O(n)
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    
def reverseArray(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseArray(arr, start + 1, end - 1)

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, 0, n - 1)
    printArray(arr, n)

# 4. Using library function Time Complexity: O(n), Space Complexity: O(1)

def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")


def reverseArray(arr, n):
    arr.reverse()              # ans = arr[::-1]  # Reverse using slicing

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)
    printArray(arr, n)    
    