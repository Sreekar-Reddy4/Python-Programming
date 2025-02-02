#Algorithm to rotate the array elements to the left by k elements in an optimal way.
#Time complexity: O(n)
#Space complexity: O(1)
# 1 Reverse the first k elements of the array
# 2 Reverse the last n-k elements of the array
# 3 Reverse the whole array


def reverse(arr, start, end):
    """Function to reverse the array elements between indices start and end."""
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def rotate_elements_to_left(arr, n, k):
    """Function to rotate k elements to the left."""
    # Reverse first k elements
    reverse(arr, 0,n-k-1)
    # Reverse last n-k elements
    reverse(arr, n-k, n - 1)
    # Reverse the whole array
    reverse(arr, 0, n - 1)

if __name__ == "__main__":
    arr = [3,7,8,9,10,11]
    n = len(arr)
    k = 3
    rotate_elements_to_left(arr, n, k)
    print("After rotating the k elements to left:", arr)
