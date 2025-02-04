# Given a string, check if the string is palindrome or not.  (leet code - easy)

# 1. using loop   Time Complexity:  O(N), Space Complexity: O(1)

def isPalindrome(s):
    left = 0
    right = len(s)-1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

if __name__ == "__main__":
    str = "A man, a plan, a canal: Panama"
    ans = isPalindrome(str)
    if ans == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

# 2. Recursive Approach  Time Complexity:  O(N), Space Complexity: O(n)
def isPalindromeRecursive(s, left, right):
    # Base Case: If pointers cross, it's a palindrome
    if left >= right:
        return True

    # Check first and last characters
    if s[left] != s[right]:
        return False

    # Recursive Case: Check the remaining substring
    return isPalindromeRecursive(s, left + 1, right - 1)

def isPalindrome(s):
    return isPalindromeRecursive(s, 0, len(s) - 1)

s = "madam"
print(isPalindrome(s))  # Output: True

s = "hello"
print(isPalindrome(s))  # Output: False
