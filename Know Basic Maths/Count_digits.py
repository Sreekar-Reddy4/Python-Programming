#  Given an integer N, return the number of digits in N.

# 1. Brute Force Approach -> Time Complexity: O(log10N + 1), Space Complexity : O(1)
def countDigits(n):
    count = 0
    
    while n > 0:
        count = count + 1
        n = n // 10
    return count


if __name__ == "__main__":
    N = 329823
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)

# 2. Optimal Approach -> Time Complexity: O(1), Space Complexity : O(1)

import math

# Calculate the count of digits in 'n'
# using logarithmic operation log10(n) + 1.
def countDigits(n):
    # Initialize a variable 'cnt' to
    # store the count of digits.
    cnt = int(math.log10(n) + 1)

    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
    # Return the count of digits in 'n'.
    return cnt
if __name__ == "__main__":
    N = 3216807
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)    