#Example 1:
# Input Format:
#  arr = [4,5,6,7,0,1,2,3]
# Result:
#  4
# Explanation:
#  The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

#Approach: Find the minimum element in the rotated sorted array and return its index as the result.Where index determines number of rotations.
#Time complexity: O(logn)
#Space complexity: O(1)




def min_sorted(arr,n):
    low = 0
    high = n-1
    ans = float('inf')
    res = 0
    
    while low<=high:
        mid = low+high//2
        if arr[low]<=arr[high]:
            ans = min(ans,arr[low])
            res = low
            break
        if arr[low]<=arr[mid]:
            ans = min(ans,arr[low])
            res = low
            low=mid+1
        else:
            ans = min(ans,arr[mid])
            res = mid
            high=mid-1
    return res

out = min_sorted([3,4,5,1,2],5)
print(out)