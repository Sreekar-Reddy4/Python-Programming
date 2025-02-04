# Print numbers from N to 1 (space separated) without the help of loops.
def printNosReverse(n):
    if n == 0:
        return
    print(n, end=" ")  # Print current number
    printNosReverse(n - 1)  # Recursive call
N = 10
printNosReverse(N)
