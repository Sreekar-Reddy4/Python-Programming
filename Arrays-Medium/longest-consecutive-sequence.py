# [100, 200, 1, 3, 2, 4]

# Output:
#  4

# Explanation:
#  The longest consecutive subsequence is 1, 2, 3, and 4.

def long_cons_arr(arr):
    counter=0
    for i in range(len(arr)):
        if arr[i]+1 in arr or arr[i]-1 in arr:
            counter+=1
    return counter

print(long_cons_arr([100,200,1,2,3,4]))