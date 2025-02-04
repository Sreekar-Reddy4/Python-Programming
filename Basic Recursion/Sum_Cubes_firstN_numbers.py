# Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

# using recursion
def fun(n):
    if n==0:
        return 0
    return (n**3) + fun(n-1)
n=7
print(fun(n))    
