def sir(arr,n,target):
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if low == high:
            # arr[mid]=target
            ans = mid
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            ans = mid
    return ans

res = sir([1,2,4,7],4,6)
print(res)
