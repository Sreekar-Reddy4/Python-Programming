# Input: arr = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation: In the array, the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 is -1, since it does not exist.


def next_greater_element(arr):
    n=len(arr)
    res=[0]*n
    st=[]
    
    for i in range(n-1,-1,-1):
        
        while st and st[-1]<=arr[i]:
            st.pop()
        
        if not st:
            res[i]=-1
        else:
            res[i]=st[-1]
        
        st.append(arr[i])
        
    return res

print(next_greater_element([1, 3, 2, 4]))