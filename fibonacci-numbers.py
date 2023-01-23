
def fibonacci_recursion(n):

    # BASE CASE
    if n == 0:
        return 1
    
    if n == 1:
        return 1
    
    # O(2^n) -exponential time complexity
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# print(fibonacci_recursion(5))


# top-down approach
def fibonacci_memoization(n, table):

    # O(N) -space complexity
    if n not in table:
        table[n] = fibonacci_memoization(n-1, table) + fibonacci_memoization(n-2, table)
    
    # O(1) -constant time complexity
    return table[n]


# bottom-up approach
def fibonacci_tabulation(n, table):

    for i in range(2, n + 1):
        table[i] = table[i -1] + table[i-2]
    
    # O(N) -linear time complexity
    return table[n]



# this is how we define the base case
t = {0: 1, 1:1}

# print(fibonacci_memoization(5, t))
print(fibonacci_tabulation(5, t))