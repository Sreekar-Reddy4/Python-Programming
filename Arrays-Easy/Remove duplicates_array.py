def remove_duplicates(arr,n):
    i = 0
    for j in range(1,n):
        if arr[i]!=arr[j]:
            i+=1
            arr[i] = arr[j]
    return i+1

if __name__ == "__main__":
    arr = [1,2,2,3,4,4,4,5,5]
    n = len(arr)
    print(remove_duplicates(arr,n))