def largest_element_arr_recursive(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max = arr[i]
    return max

sol = largest_element_arr_recursive([2,5,1,3,0])
print(sol)