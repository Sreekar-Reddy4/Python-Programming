def left_rotate_arr(arr,n):
    temp = [0]*n
    for i in range(1,n):
        temp[i-1] = arr[i]
    temp[n-1] = arr[0]
    return temp

sol = left_rotate_arr([1,2,3,4,5],5)
print(sol)
