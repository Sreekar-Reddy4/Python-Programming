# Trapping Rain Water - Brute Force Approach
# Time Complexity: O(N^2) because for each element we traverse the array twice
# Space Complexity: O(1) as we are using only a few variables

#Formula: water trapped at index i = min(max height to the left, max height to the right) - height[i]
# Example heights
# h = [0,1,0,2,1,0,1,3,2,1,2,1]
# Example heights
# h = [4,2,0,3,2,5]




h = [0,1,0,2,1,0,1,3,2,1,2,1]
total = 0
n = len(h)

for i in range(len(h)):
    lmax = 0
    rmax = 0
    
    for j in range(i+1):
        if h[j]>lmax:
            lmax=h[j]
    
    for k in range(i,n):
        if h[k]>rmax:
            rmax=h[k]
    
    total+=min(lmax,rmax)-h[i]

print(total)