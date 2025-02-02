#Time complexity - O(nlogn)
#Space Complexity - O(1)

def getElements(arr, n):
    if n == 0 or n == 1:                   #edge case when only one element is present in array
        print(-1, -1)

    else:                       
        arr.sort()
        small = arr[1]
        large = arr[n-2]
        print("Second smallest is", small)
        print("Second largest is", large)




if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    n = len(arr)
    getElements(arr, n)

