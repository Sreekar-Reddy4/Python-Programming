# # Leet Code - Medium - Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

def reverse(x: int) -> int:
    # Define the 32-bit signed integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Check if the number is negative
    sign = -1 if x < 0 else 1
    x = abs(x)

    # Reverse the digits
    reversed_x = 0
    while x != 0:
        # Get the last digit
        digit = x % 10
        # Append it to the reversed number
        reversed_x = reversed_x * 10 + digit
        # Remove the last digit
        x //= 10

    # Restore the sign
    reversed_x *= sign

    # Check if the reversed number is within the 32-bit signed integer range
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0

    return reversed_x
print(reverse(-143))
