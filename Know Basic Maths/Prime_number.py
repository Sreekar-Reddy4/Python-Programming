# Given an integer N, check whether it is prime or not. 
# A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

# 1. Brute Force Approach Time Complexity: O(N), Space Complexity : O(1)

def checkPrime(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt = cnt + 1

    # If the number of factors is exactly 2
    if cnt == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 9
    isPrime = checkPrime(n)
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

# 2.  Optimal Approach Time Complexity: O(sqrt(N)), Space Complexity : O(1)

                                                   
import math

def checkPrime(n):
    cnt = 0

    # Loop through numbers from 1 till the square root of n.
    for i in range(1, int(math.sqrt(n)) + 1):
        
        if n % i == 0:
            cnt = cnt + 1

            # If n is not a perfect square, count its reciprocal factor.
            if n // i != i:
                cnt = cnt + 1
    if cnt == 2:
        return True
    else:
        return False

# Main function
def main():
    n = 1483
    isPrime = checkPrime(n)
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

if __name__ == "__main__":
    main()

                                
                                  
                                
                            