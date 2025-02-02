arr = [1, 0, 1, 1, 0, 1]
max_count = 0
count = 0
for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count)