arr=[1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n=len(arr)
i=0
for i in range(n):
    for j in range(n-1):
        if arr[j]==0:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            j+=1
        else:
            j+=1
print(arr)