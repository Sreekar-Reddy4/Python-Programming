# Given a positive integer N, print the digits of N separately.
   
# 1. Optimal Approach -> Time Complexity: O(log10N + 1), Space Complexity : O(log10N + 1)

import math

def extractDigits(N):
    ans = []
   
    while N > 0:
        
        lastDigit = N % 10  

        ans.append(lastDigit) 
        
        N = math.floor(N / 10)  # N = N//10 without math ***
    
    ans.reverse()
    
    return ans


def main():
    N = 12345
    print("N:", N)
    digits = extractDigits(N)
    print("Extracted Digits:", end=" ")
    for num in digits:
        print(num, end=" ")
    print()


if __name__ == "__main__":
    main()