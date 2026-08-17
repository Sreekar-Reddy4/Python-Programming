

# Next Greater Element II - Optimal Approach
# Time Complexity: O(4N) because each element is pushed and popped at most twice , forloop 2N iterations
# Space Complexity: O(2N) becas use of result array and stack

arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
n = len(arr)
print(n)
res=[-1]*n
print(res)
st=[]
for i in range(2*n-1,-1,-1):
    ind = i%n
    print(i)
    while st and st[-1]<=arr[ind]:
        st.pop()
    if i<n and st:
        res[i]=st[-1]
    st.append(arr[ind])
print(res) 