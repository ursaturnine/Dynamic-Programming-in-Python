""" Write a number fib(n) that takes in a number as an argument.
The number should return the n-th number of the fibonacci sequence
"""

# this function is slower with larger input values
def fibonacci(n):
    if n <=2:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n-2)

# this function does not slow down with larger input values
def fibonacci_memoization(n, table = {}):
    if n in table:
        return table[n]
    if n <= 2:
        return 1
    table[n] = fibonacci_memoization(n-1, table) +fibonacci_memoization(n -2, table)
    return table[n]


if __name__ == '__main__':
    print(fibonacci_memoization(50))
