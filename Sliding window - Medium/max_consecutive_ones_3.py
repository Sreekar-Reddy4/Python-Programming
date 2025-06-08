# Given a binary array nums and an integer k, flip at most k 0's.

# Return the maximum number of consecutive 1's after performing the flipping operation.


# Examples:

# Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3

# Output : 10

# Explanation : The maximum number of consecutive 1's are obtained only if we flip the 0's present at position 3, 4, 5 (0 base indexing).

# The array after flipping becomes [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0].

# The number of consecutive 1's is 10.

# Input : nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3

# Output : 9

# Explanation : The underlines 1's are obtained by flipping 0's in the new array.

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1].

# The number of consecutive 1's is 9.


def longest_consec_ones(arr,k):
    left = 0
    max_len = 0
    zero_count = 0
    for right in range(len(arr)):
        if arr[right]==0:
            zero_count+=1
        
        while zero_count > k:
            if arr[left]==0:
                zero_count-=1
            left+=1
        
        max_len = max(max_len,right-left+1)
    
    return max_len

result = longest_consec_ones([0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],3)
print(result)