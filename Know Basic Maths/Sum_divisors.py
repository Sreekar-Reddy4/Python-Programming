# Given an integer N, return all divisors of N.
# 1. Brute Force Approach Time Complexity: O(N), Space Complexity: O(N)
def sum_of_divisors(n):
    total_sum = 0
    #divisors=[]
    for i in range(1, n + 1):
         #if n % i == 0:
            #divisors.append(i)  # Add divisor to the list
        div_sum = sum(j for j in range(1, i + 1) if i % j == 0)  # Sum of divisors of i
        total_sum += div_sum
    
    return total_sum

n = 10
print(sum_of_divisors(n))  # Output: 87

# 2. Better Approach Time Complexity: O(N)
def sum_of_F(n):
    total_sum = 0
    
    for j in range(1, n + 1):
        total_sum += j * (n // j)
    
    return total_sum

n = 10
print(sum_of_F(n))  # Output: 87 

# 3. Optimal Approach Time Complexity: O(sqrt(N)), Space Complexity : O(2*sqrt(N))
                                
# this will only return all the divisors but not the sum                  
import math

def findDivisors(n):
    # Initialize an empty
    # list to store the divisors
    divisors = [] 

    # Iterate up to the square
    # root of n to find divisors
    # Calculate the square root of n
    sqrtN = int(math.sqrt(n)) 
    
    # Loop from 1 to the
    # square root of n
    for i in range(1, sqrtN + 1): 
        # Check if i divides n
        # without leaving a remainder
        if n % i == 0: 
            # Add divisor i to the list
            divisors.append(i) 

            # Add the counterpart divisor
            # if it's different from i
            if i != n // i:
                # Add the counterpart
                # divisor to the list
                divisors.append(n // i) 
    
    # Return the list of divisors
    return divisors 

if __name__ == "__main__":
    number = 12
    divisors = findDivisors(number)

    print("Divisors of", number, "are:", end=" ")
    for divisor in divisors:
        print(divisor, end=" ")
    print()

                                
                            