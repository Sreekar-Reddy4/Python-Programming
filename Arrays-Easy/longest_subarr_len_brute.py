#Time Complexity: O(n^2)
#Space Complexity: O(1)

arr = [2,3,5]
n = len(arr)
k = 5
max_len = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += arr[j]
        if sum == k:
            max_len = max(max_len, j-i+1)
print(max_len)