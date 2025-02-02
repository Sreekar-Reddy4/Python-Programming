# Leet Code - Easy - Palindrome Number
# Given an integer N, return true if it is a palindrome else return false.
# Optimal Approach Time Complexity: O(log10N + 1), Space Complexity: O(1) 
# This program works with signed integers as well eg: -121 is not a palindrome

def palindrome(n):
   
    revNum = 0
    dup = n
    while n > 0:
        lastdigit = n % 10
        
        revNum = (revNum * 10) + lastdigit
        
        n = n // 10
    if dup == revNum:
        return True
    else:
        return False


def main():
    number = 121

    if palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")


if __name__ == "__main__":
    main()