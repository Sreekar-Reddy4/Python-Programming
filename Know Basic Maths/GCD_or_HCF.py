# Given two integers N1 and N2, find their greatest common divisor.

# 1. Brute Force Approach Time Complexity: O(min(N1, N2)), Space Complexity: O(1)

def find_gcd(n1, n2):
    gcd = 1
    for i in range(1, min(n1, n2) + 1):
        # Check if i is a common factor of both n1 and n2
        if n1 % i == 0 and n2 % i == 0:
            # Update gcd to the current common factor i
            gcd = i

    return gcd

if __name__ == "__main__":
    n1, n2 = 20, 15
    gcd = find_gcd(n1, n2)

    print("GCD of", n1, "and", n2, "is:", gcd)

# 2. Better Approach -> The time complexity of this approach remains O(min(N1, N2)) but in practice, it will execute fewer iterations on average.

                                
def findGcd(n1, n2):
    # Iterate from the minimum of n1 and n2 down to 1(because the GCD cannot exceed the smaller number)
    
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    # If no common factors are found, return 1 (as 1 is always a divisor of any number)
    
    return 1


def main():
    n1 = 20
    n2 = 15
    gcd = findGcd(n1, n2)

    print("GCD of", n1, "and", n2, "is:", gcd)


if __name__ == "__main__":
    main()
    
                                                         
# 3. Optimal Approach -> Time Complexity: O(min(N1, N2)), Space Complexity: O(1)

# The Euclidean Algorithm is a method for finding the greatest common divisor of two numbers. 
# It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.
                                
def find_gcd(a, b):

    while a > 0 and b > 0:
        # If a is greater than b,
        # subtract b from a and update a
        if a > b:
            # Update a to the remainder
            # of a divided by b
            a = a % b
        # If b is greater than or equal
        # to a, subtract a from b and update b
        else:
            # Update b to the remainder
            # of b divided by a
            b = b % a
    # Check if a becomes 0,
    # if so, return b as the GCD
    if a == 0:
        return b
    # If a is not 0,
    # return a as the GCD
    return a


def main():
    n1 = 20
    n2 = 15
    gcd = find_gcd(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")


if __name__ == "__main__":
    main()
    
                                
                            