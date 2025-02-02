#Sort the array first
#return last element of the array

def brute_arr_largest(arr):
    arr.sort()
    return arr[-1]

sol = brute_arr_largest([2,5,1,3,0])
print(sol)