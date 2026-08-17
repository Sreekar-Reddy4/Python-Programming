# Example 2:
# Input:
#  arr = [5, 7, 1, 7, 6, 0]
# Output:
#  [7, -1, 7, -1, 7, 5]
# Explanation:
#  For the first element in arr i.e, 5, the greater element which comes next to it while traversing and is closest to it is 7.
#  Now for the second element i.e, 7, there is no greater number and hence -1 is it’s next greater element (NGE). 
#  For the last element i.e, 0, the next greater element is again 5.
# Similarly, we got the NGEs for all other elements present in arr.

#brute force approach:-
#[Time Complexity: O(n^2), Space Complexity: O(1)]
#Approach:- via nested loops for each element, check the next elements in circular manner to find the next greater element.
#virtually extend the array by concatenating it to itself and use modulo operation to simulate circular behavior.
# Example:- [5, 7, 1, 7, 6, 0 ,5, 7, 1, 7, 6, 0] - virtually extended array 
# Indices    0 1  2  3  4  5   6  7  8  9 10 11 
# suppose for element at index 0 i.e. 7 can check next elements at indices 1,2,3,4,5 to find the next greater element.

arr = [5, 7, 1, 7, 6, 0]
nge = [-1] * len(arr)  # Initialize the result array with -1s
for i in range(len(arr)):
    for j in range(i+1, i + len(arr)-2):
        ind=j%len(arr)
        if arr[ind] > arr[i]:
            nge[i] = arr[ind]
            break
print(nge)