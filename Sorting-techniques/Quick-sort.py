def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: Already sorted

    pivot = arr[len(arr) // 2]  # Choosing middle element as pivot
    left = [x for x in arr if x < pivot]   # Elements smaller than pivot
    middle = [x for x in arr if x == pivot] # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sorting


sol = quick_sort([6, 9, 11, 51, 10])
print(sol)