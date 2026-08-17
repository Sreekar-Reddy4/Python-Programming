#Optimal approach using two pointers
# Time Complexity: O(N) as we traverse the array only once
# Space Complexity: O(1) as we are using only a few variables

#h = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height) -> int:
    left, right = 0, len(height) - 1
    lmax = 0
    rmax = 0
    total = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= lmax:
                lmax = height[left]
            else:
                total += lmax - height[left]
            left += 1
        else:
            if height[right] >= rmax:
                rmax = height[right]
            else:
                total += rmax - height[right]
            right -= 1
    return total
h = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(h))