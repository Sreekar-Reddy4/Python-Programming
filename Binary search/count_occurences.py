### Count Occurrences in Sorted Array with duplicates ###
# N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
# Output
# : 4
# Explanation:
#  3 is occurring 4 times in 
# the given array so it is our answer

def first_occurence(arr,n,x):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]>=x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# res = first_occurence([3,4,13,13,13,20,40],7,13)
# print(res)


def last_occurence(arr,n,x):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]<=x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

# res1 = last_occurence([3,4,13,13,13,20,40],7,13)

def count_occurences(arr,n,x):
    first = first_occurence(arr,n,x)
    last = last_occurence(arr,n,x)
    return last - first + 1

res = count_occurences([2, 2 , 3 , 3 , 3 , 3 , 4],7,3)
print(res)