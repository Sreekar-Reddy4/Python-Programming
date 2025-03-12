# Example 1:
# Input Format:
#  arr = [4,5,6,7,0,1,2,3]
# Result:
#  0
# Explanation:
#  Here, the element 0 is the minimum element in the array

def min_sorted(arr,n):
    low = 0
    high = n-1
    ans = float('inf')
    
    while low<=high:
        mid = low+high//2
        if arr[low]<=arr[high]:  # if the array is already sorted
            ans = min(ans,arr[low])
            break
        if arr[low]<=arr[mid]:   # if the left part is sorted
            ans = min(ans,arr[low])
            low=mid+1
        else:                    # if the right part is sorted
            ans = min(ans,arr[mid])
            high=mid-1
    return ans

res = min_sorted([4,5,6,7,0,1,2,3],8)
print(res)