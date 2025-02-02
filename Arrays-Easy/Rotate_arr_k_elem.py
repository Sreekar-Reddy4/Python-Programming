arr = [1,2,3,4,5,6,7]
n=len(arr)
k = 2
arr = arr[n-k:]+arr[:n-k]
print(arr)