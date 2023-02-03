"""Write a function, howSum(targetSum, numbers), that takes
in a targetSum and an array of numbers as arguments.

The function should return an array containing any combination
of elements that add up to exactly the targetSum. If there is no 
combination that adds up to the targetSum, then return null.
"""

# O(n^m)
def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num

        # howSum returns a list or None
        remainderResult = howSum(remainder, numbers)
        if remainderResult is not None:
            return remainderResult + [num]
    

    return None

# O(NM)
# dynamic programming approach
def howSumDynamic(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num

        # howSum returns a list or None
        remainderResult = howSumDynamic(remainder, numbers, memo)
        if remainderResult is not None:
            # save return results from recursive solution to memo
            memo[targetSum] = remainderResult + [num]
            return memo[targetSum]
    
    memo[targetSum] = None
    return None


print(howSumDynamic(7, [2,3])) # [3, 2, 2]
print(howSumDynamic(7, [5,4,3, 7])) # [3,4]
print(howSumDynamic(7, [2,4])) # None
print(howSumDynamic(8, [2,3, 5])) # [2, 2, 2, 2]
print(howSumDynamic(300, [7, 14])) # 