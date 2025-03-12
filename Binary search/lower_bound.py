# What is Lower Bound?
# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.






# Input Format:
#  N = 4, arr[] = {1,2,2,3}, x = 2
# Result:
#  1
# Explanation:
#  Index 1 is the smallest index such that arr[1] >= x


def lwr_bnd(arr,n,x):
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = low+high//2
        if arr[mid]>=x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

res = lwr_bnd([1,2,2,3],4,2)
print(res)

