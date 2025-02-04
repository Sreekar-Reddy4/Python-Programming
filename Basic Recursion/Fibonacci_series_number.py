#  Given an integer N. Print the Fibonacci series up to the Nth term.  (Leet Code - Easy)

# 1.Native Approach using recursion Time Complexity: O(2ⁿ) (Exponential), space complexity: o(n)

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def printFibonacciSeries(n):
    for i in range(n):
        print(fib(i), end=" ")  # Print each Fibonacci number

# Example Usage
n = 10
print("Fibonacci Series:")
printFibonacciSeries(n)

# 2. Optimized Approach: Using Memoization  Time Complexity: O(n)

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def printFibonacciSeries(n):
    for i in range(n):
        print(fib_memo(i), end=" ")

n = 10
print("Fibonacci Series:")
printFibonacciSeries(n)


