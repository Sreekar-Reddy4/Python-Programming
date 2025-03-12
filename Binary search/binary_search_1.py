### Binary Search Algorithm ###
# Time Complexity: O(log n)
# Space Complexity: O(1)

def binary_search(list,target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid =low+high//2
        if target > list[mid]:
            low = mid + 1   
        elif target < list[mid]:
            high = mid - 1
        else:
            return mid
    return None

res = binary_search([1,2,3,4,5,6,7,8,9,10], 5)
print(res)