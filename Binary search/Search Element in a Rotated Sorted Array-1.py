###Example 1:
# Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
# Result: 4
# Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. 
# Thus, we get output as 4, which is the index at which 0 is present in the array.

def sorted_arr(arr,n,x):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = low + (high-low)//2
        if arr[low]<=arr[mid]:
            if arr[low]<=x and x<=arr[mid]:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=x and x<=arr[high]:
                ans = mid
                low = mid+1
            else:
                high = mid-1
    return ans

arr = [4,5,6,7,0,1,2,3]
n = len(arr)
x = 0
print(sorted_arr(arr,n,x))
    
