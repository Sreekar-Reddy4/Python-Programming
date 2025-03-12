def floor(arr,n,x):
    low = 0
    high = n-1
    ans = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid]<=x:
            ans = arr[mid]
            low = mid+1
        else:
            high = mid-1
    return ans

res = floor([3, 4, 4, 7, 8, 10],6,5)
print(res)

## ciel is nothing but lower bound
def ciel(arr,n,x):
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if arr[mid]>=x:
            ans = arr[mid]
            high = mid-1
        else:
            low = mid+1
    return ans

res2 = ciel([3, 4, 4, 7, 8, 10],6,5)
print(res2)