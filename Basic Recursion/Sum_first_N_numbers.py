# Sum of first N Natural Numbers
# 1. Using Formula sum = n*(n+1)/2  Time Complexity: O(1), Space Complexity: O(1)
n=6
a=int(n*(n+1)/2)
print("Sum of first {} numbers: {}".format(n,a))

# 2. Using Loops  Time Complexity: O(N), Space Complexity: O(1)
n=6
sum = 0
for i in range(1,n+1):
    sum += i
print("Sum of first {} numbers: {}".format(n,sum))

# 3. using recursion Time Complexity: O(N), Space Complexity: O(N)

def fun(n):
    if n==0:
        return 0
    return n + fun(n-1)
n=6
print(fun(n))