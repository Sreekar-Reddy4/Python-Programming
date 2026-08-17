arr = [7, 4, 1, 5, 3]
n = len(arr)
for i in range(n-1,-1,-1):
    did_swap = 0
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            did_swap=1
    
    if did_swap == 0:
        break
print(arr)