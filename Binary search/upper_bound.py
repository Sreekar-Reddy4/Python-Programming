# What is Upper Bound?
# The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.

# The upper bound is the smallest index, ind, where arr[ind] > x.

# But if any such index is not found, the upper bound algorithm returns n i.e. size of the given array. 
# The main difference between the lower and upper bound is in the condition. For the lower bound the condition was arr[ind] >= x and here, in the case of the upper bound, it is arr[ind] > x.



# Input Format:
# Example 1:
# Input Format:
#  N = 4, arr[] = {1,2,2,3}, x = 2
# Result:
#  3
# Explanation:
#  Index 3 is the smallest index such that arr[3] > x.


def upr_bnd(arr,n,x):
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if arr[mid]>x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans


res = upr_bnd([1,2,2,3],4,2)
print(res)