#Example 1: 

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]

# Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] 
# satisfy the condition of summing up to zero with i!=j!=k



nums = [-1,0,1,2,-1,-4]
st = set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k] == 0:
                temp = [nums[i],nums[j],nums[k]]
                temp.sort()
                st.add(tuple(temp))

print(st)
ans = [list(i) for i in st]
print(ans)
