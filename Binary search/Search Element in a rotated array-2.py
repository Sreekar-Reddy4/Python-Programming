# Input Format:
#  arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
# Result:
#  True
# Explanation:
#  The element 3 is present in the array. So, the answer is True.

def search_rotated_arr(arr,n,k):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        if arr[low]<=arr[mid]:
            ans = mid
            if arr[low]<=k and k<=arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=k and k<=arr[high]:
                ans = mid
                low = mid+1
            else:
                high = mid-1
    return ans

res = search_rotated_arr([7, 8, 1, 2, 3, 3, 3, 4, 5, 6],10,3)
if res != -1:
    print(True)
else:
    print(False)