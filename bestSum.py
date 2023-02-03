"""Write a function, bestSum(targetSum, numbers), that takes in a
targetSum and an array of numbers as arguments.

The function should return an array containing the shortest
combination of numbers that add up to exactly the targetSum.
"""

def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortest = None

    # checks all branches
    for num in numbers:
        remainder = targetSum - num
        remainderCombo = bestSum(remainder, numbers)
        if remainderCombo is not None:
            combination = remainderCombo + [num]
            # replace original None value w first combo found
            if shortest == None or len(combination) < len(shortest):
                shortest = combination
    
    return shortest

def bestSumDynamic(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    
    if targetSum in memo:
        return memo[targetSum]
        
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortest = None

    # checks all branches
    for num in numbers:
        remainder = targetSum - num
        remainderCombo = bestSumDynamic(remainder, numbers, memo)
        if remainderCombo is not None:
            combination = remainderCombo + [num]
            # replace original None value w first combo found
            if shortest == None or len(combination) < len(shortest):
                shortest = combination
    
    memo[targetSum] = shortest
    return shortest




print(bestSumDynamic(7, [5,4,3, 7]))  # [7]
print(bestSumDynamic(8, [2,3, 5]))  # [3, 5]
print(bestSumDynamic(8, [1,4, 5]))  # [4, 4]
print(bestSumDynamic(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]