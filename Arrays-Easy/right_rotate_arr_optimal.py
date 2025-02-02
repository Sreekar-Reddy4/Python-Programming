#Algorithm to rotate the array to right by k elements
#Time complexity: O(n)
#Space complexity: O(1)
#1. Reverse the last k elements of the array
#2. Reverse the first n-k elements of the array
#3. Reverse the whole array



def reverse_arr(arr,i,j):
    i=0
    j=len(arr)-1
    while i<=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

def right_rotate_arr(arr,n,k):
    reverse_arr(arr,n-k,n-k-1)
    reverse_arr(arr,0,n-k-1)
    reverse_arr(arr,0,n-1)
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    k = 2
    right_rotate_arr(arr, n, k)
    print("After rotating the k elements to right:", arr)
