#Given two integers a and b, write a function lcm() to compute their LCM
# 1. Brute Force Approach
def lcm_bruteforce(a: int, b: int) -> int:
    # Ensure that a is the smaller number and b is the larger one
    if a > b:
        a, b = b, a
    
    # Start checking from the larger number and keep checking multiples
    multiple = b
    while multiple % a != 0:
        multiple += b
    
    return multiple
# 2. Optimal Approach (using Euclidean algorithm to compute the GCD and apply formula for LCM)
import math

def lcm(a: int, b: int) -> int:
    # Calculate LCM using the relation: LCM(a, b) = abs(a * b) // GCD(a, b)
    return abs(a * b) // math.gcd(a, b)
