# You are given an integer 'n'. Return 'true' if 'n' is an Armstrong number, and 'false' otherwise.

#An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal to the number itself. 
# For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.

# Brute Force Approach

def arm(n):
    c=0
    temp = n
    out = n
    fin=0
    while n>0: # to get count of digits
        m=n%10
        c+=1
        n//=10
    while temp>0:
        k=temp%10
        fin = fin + (k**c)
        temp = temp//10
    if fin == out:
        return True
    return False
    
s=arm(371)  
print(s)

# Optimal Approach Time Complexity: O(log10N + 1), Space Complexity: O(1)
def isArmstrong(num):
    
    k = len(str(num))
    
    sum = 0
    
    temp = num
    # Iterate through each digit of the number
    while temp > 0:
        lastdigit = temp % 10
        sum += lastdigit ** k
        temp = temp // 10
    return sum == num

def main():
    number = 153
    if isArmstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")

if __name__ == "__main__":
    main()
                           
                        
