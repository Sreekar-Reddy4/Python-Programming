# You are given a number ’n’.
# Find the number of digits of ‘n’ that evenly divide ‘n’.
# Note:
# A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.

# Method 1: Converting into string
def count_evenly_dividing_digits(n):
    count = 0
    for digit in str(n):  
        if digit != '0' and n % int(digit) == 0:  
            count += 1
    return count

n = 336
print(count_evenly_dividing_digits(n))  

# Method 2: Directly using given number
def count_evenly_dividing_digits(n):
    original_n = n  # Store the original number
    count = 0
    
    while n > 0:
        digit = n % 10  # Extract last digit
        if digit != 0 and original_n % digit == 0:  # Check divisibility
            count += 1
        n //= 10  # Remove last digit
    
    return count

n = 336
print(count_evenly_dividing_digits(n))  # Output: 3

